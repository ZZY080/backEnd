from fastapi import APIRouter, Request

from module.database_table.user_model import UserModel
from module.global_dict import Global
from module.http_result import HttpResult
from module.jwt_manager import JWTManager
from module.logger_ex import LoggerEx, LogLevel
from module.model.check_username_valid_model import CheckUsernameValidModel
from module.model.login_request_model import LoginRequestModel
from module.model.register_request_model import RegisterRequestModel
from module.utility import hmac_sha1


class UserController(APIRouter):
    """信息接口"""

    def __init__(self, *args, **kwargs):
        super().__init__(prefix='/user', *args, **kwargs)
        self.log = LoggerEx(self.__class__.__name__)
        if Global().debug_mode:
            self.log.set_level(LogLevel.DEBUG)
        self.log.debug(f'{self.__class__.__name__} Initializing...')

        self.add_api_route('/login', self.login, methods=['POST'], tags=['User'], name='登录')
        self.add_api_route('/register', self.register, methods=['POST'], tags=['User'], name='注册')
        self.add_api_route('/username-valid', self.is_username_valid, methods=['GET'], tags=['User'], name='检查用户名是否未注册并可用')
        self.add_api_route('/info', self.get_user_info, methods=['GET'], tags=['User'], name='获取用户信息')

    async def login(self, lrm: LoginRequestModel) -> dict:
        """登录"""
        if UserModel.is_password_correct(lrm.username, hmac_sha1(lrm.username, lrm.password)):
            return HttpResult.success(JWTManager.create_jwt(lrm.username))
        return HttpResult.no_auth('用户名或密码错误')

    async def register(self, rrm: RegisterRequestModel) -> dict:
        """注册"""
        if UserModel.is_username_exist(rrm.username):
            return HttpResult.bad_request('用户名已存在')
        encrypted_password = hmac_sha1(rrm.username, rrm.password)
        new_user = UserModel(
            username=rrm.username,
            password=encrypted_password,
            nickname=rrm.nickname
        )
        self.log.debug(f'new register user: {new_user}')
        return HttpResult.success() if new_user.save() else HttpResult.error()

    async def is_username_valid(self, cuv: CheckUsernameValidModel) -> dict:
        """检查用户名是否合法"""
        return HttpResult.success(not UserModel.is_username_exist(cuv.username))

    async def get_user_info(self, req: Request) -> dict:
        """获取用户信息"""
        user: UserModel = req.state.user
        return HttpResult.success(UserModel.get_user_information(user.username))
