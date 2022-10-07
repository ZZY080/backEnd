from fastapi import APIRouter, Request
from starlette.responses import JSONResponse

from module.database_table.user_model import UserModel
from module.global_dict import Global
from module.http_result import HttpResult
from module.logger_ex import LoggerEx, LogLevel


class AccountController(APIRouter):
    """信息接口"""

    def __init__(self, *args, **kwargs):
        super().__init__(prefix='/account', *args, **kwargs)
        self.log = LoggerEx(self.__class__.__name__)
        if Global().debug_mode:
            self.log.set_level(LogLevel.DEBUG)
        self.log.debug(f'{self.__class__.__name__} Initializing...')

        self.add_api_route(response_model=HttpResult, path='/balance', endpoint=self.get_balance,
                           methods=['GET'], name='获取用户余额')

    async def get_balance(self, req: Request) -> JSONResponse:
        """获取余额，单位：元"""
        user: UserModel = req.state.user
        return HttpResult.success(float(user.balance))
