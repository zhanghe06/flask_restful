#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: exceptions.py
@time: 2018-05-30 20:07
"""


from flask_restful import HTTPException

errors = {
    'BadRequest': {
        # 'message': 'Bad request.',
        'status': 400,
    },
    'Unauthorized': {
        'message': 'Authentication required.',
        'status': 401,
    },
    'Forbidden': {
        'message': 'Forbidden.',
        'status': 403,
    },
    'TokenNotExist': {
        'message': 'Token required.',
        'status': 403,
    },
    'TokenExpired': {
        'message': 'Token expired.',
        'status': 403,
    },
    'TokenError': {
        'message': 'Token error.',
        'status': 403,
    },
    'NotFound': {
        'message': 'Not found.',
        'status': 404,
    },
    'MethodNotAllowed': {
        'message': 'Method not allowed.',
        'status': 405,
    },
    'Conflict': {
        'message': 'Conflict.',
        'status': 409,
        'extra': 'Resource already exists.',
    },
    'Gone': {
        'message': 'Gone.',
        'status': 410,
        'extra': 'Resource has gone.',
    },
    'PreconditionFailed': {
        'message': 'Precondition failed.',
        'status': 412,
    },
    'RequestEntityTooLarge': {
        'message': 'Request entity too large.',
        'status': 413,
    },
    'UnsupportedMediaType': {
        'message': 'Unsupported media type.',
        'status': 415,
    },
    'ServiceUnavailable': {
        'message': 'Service unavailable.',
        'status': 503,
    },
}


class BadRequest(HTTPException):
    pass


class Unauthorized(HTTPException):
    pass


class Forbidden(HTTPException):
    pass


class TokenNotExist(HTTPException):
    pass


class TokenExpired(HTTPException):
    pass


class TokenError(HTTPException):
    pass


class NotFound(HTTPException):
    pass


class MethodNotAllowed(HTTPException):
    pass


class Conflict(HTTPException):
    pass


class Gone(HTTPException):
    pass


class PreconditionFailed(HTTPException):
    pass


class RequestEntityTooLarge(HTTPException):
    pass


class UnsupportedMediaType(HTTPException):
    pass


class ServiceUnavailable(HTTPException):
    pass
