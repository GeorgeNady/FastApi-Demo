# from dataclasses import dataclass
#
#
# @dataclass
# class BaseResponse:
#     success: bool
#     data: object
#     message: str
#
#     def __init__(self, success: bool, data: object, message: str):
#         self.success = success
#         self.data = data
#         self.message = message
#
#     def json(self) -> dict:
#         return {
#             'success': self.success,
#             'data': self.data,
#             'message': self.message
#         }
