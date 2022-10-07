from fastapi import APIRouter, Request, Body
from starlette.responses import JSONResponse

from module.database_table.user_model import UserModel
from module.global_dict import Global
from module.http_result import HttpResult
from module.logger_ex import LoggerEx, LogLevel
from module.model.transfer_model import TransferModel


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
        self.add_api_route(response_model=HttpResult, path='/transfer', endpoint=self.create_transfer,
                           methods=['POST'], name='转账')
        self.add_api_route(response_model=HttpResult, path='/balance', endpoint=self.change_balance,
                           methods=['PUT'], name='修改余额')

    async def get_balance(self, req: Request) -> JSONResponse:
        """获取余额，单位：元"""
        user: UserModel = req.state.user
        self.log.info(f'check balance: {user.username}')
        return HttpResult.success(float(user.balance))

    async def create_transfer(self, tm: TransferModel, req: Request) -> JSONResponse:
        """创建转账"""
        user: UserModel = req.state.user
        if user.balance < tm.amount:
            return HttpResult.bad_request('余额不足')
        if tm.amount <= 0:
            return HttpResult.bad_request('转账金额必须大于0')
        if tm.amount > 1000000:
            return HttpResult.bad_request('转账金额不能大于1000000')
        if tm.target_username == user.id:
            return HttpResult.bad_request('不能给自己转账')
        target_user = UserModel.get_user_by_name(tm.target_username)
        if target_user is None:
            return HttpResult.bad_request('目标用户不存在')
        user.balance -= tm.amount
        target_user.balance += tm.amount
        user.save(update=True)
        target_user.save(update=True)
        self.log.info(f'transfer: {user.username} -> {target_user.username} {tm.amount}')
        return HttpResult.success()

    async def change_balance(self, username: str, amount: float) -> JSONResponse:
        """
        修改余额

        **注意：此接口仅用于测试**
        """
        user = UserModel.get_user_by_name(username)
        if user is None:
            return HttpResult.bad_request('用户不存在')
        user.balance += amount
        user.save(update=True)
        return HttpResult.success()
