import time
from typing import Union

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

from module.constants import APP_NAME
from module.global_dict import Global
from module.http_result import HttpResult
from module.logger_ex import LoggerEx, LogLevel
from module.singleton_type import SingletonType


class HttpServer(FastAPI, metaclass=SingletonType):

    def __init__(self):
        """初始化"""
        super().__init__(docs_url='/docs', redoc_url=None, title=APP_NAME)  # 关闭 redoc
        self.log = LoggerEx(self.__class__.__name__)
        if Global().debug_mode:
            self.log.set_level(LogLevel.DEBUG)
        self.log.debug(f'{self.__class__.__name__} initializing...')

        self.add_event_handler('startup', func=self.server_startup)
        self.add_event_handler('shutdown', func=self.server_shutdown)
        self.add_middleware(BaseHTTPMiddleware, dispatch=self.http_middleware)
        self.add_exception_handler(HTTPException, handler=self.exception_handler_ex)
        self.add_exception_handler(RequestValidationError, handler=self.exception_handler_ex)

        self.router.add_api_route('/', self.route_root, methods=['GET', 'POST'])

    @staticmethod
    async def exception_handler_ex(_: Request, exc: Union[HTTPException, RequestValidationError]) -> JSONResponse:
        """异常处理"""
        headers = getattr(exc, 'headers', None)
        if isinstance(exc, HTTPException):
            if exc.status_code == 404:
                content = HttpResult.not_found(exc.detail)
            else:
                content = HttpResult.error(exc.detail)
            return JSONResponse(content=content, status_code=exc.status_code, headers=headers)
        return JSONResponse(content=HttpResult.bad_request(), status_code=400, headers=headers)

    async def server_startup(self) -> None:
        """事件 服务启动"""
        self.log.debug('HttpServer startup.')

    async def server_shutdown(self) -> None:
        """事件 服务关闭"""
        self.log.debug('HttpServer shutdown.')

    async def http_middleware(self, request: Request, call_next) -> JSONResponse:
        """请求中间件"""
        self.log.debug(f'{request.method:.4s} {request.url.path} {request.query_params}')
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers['X-Process-Time'] = str(process_time)
        self.log.debug(f'{response.status_code}  Process Time: {process_time:.3f}s')
        return response

    @staticmethod
    async def route_root() -> dict:
        """根路由"""
        return HttpResult.success(f'This is {APP_NAME}!')
