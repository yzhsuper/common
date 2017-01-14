# -*- coding: utf-8 -*-

import logging
import os
from .common import *
import raven

# Secret key
# This is used to provide cryptographic signing, and should be set
# to a unique, unpredictable value.
SECRET_KEY = 'LvwqiBrC92nmOetVcHiYLgho1l2BcVY7Y4Rgeqp0zh66TN1V'

##################################################################
# Debug settings
##################################################################

# Root URLs module
ROOT_URLCONF = 'csgo-unpack.urls'

# WSGI application
WSGI_APPLICATION = 'csgo-unpack.wsgi.application'
# Set debug
DEBUG = True

# Turns on/off template debug mode.
# TEMPLATE_DEBUG = DEBUG

##################################################################
# Databases settings
##################################################################

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': '/opt/dev/db/development.sqlite'
    # },
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    #     'NAME': 'csgo',  # Or path to database file if using sqlite3.
    #     'USER': 'gogogo',
    #     'PASSWORD': '123456',
    #     'HOST': '192.168.0.118',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
    #     'PORT': '3306',  # Set to empty string for default.
    # },
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    #     'NAME': 'csgo',  # Or path to database file if using sqlite3.
    #     'USER': 'gogogo',
    #     'PASSWORD': 'M3*UDLTH6=EEWK.',
    #     'HOST': '172.16.20.181',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
    #     'PORT': '3306',  # Set to empty string for default.
    # },
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        #'NAME': 'csgodb',  # Or path to database file if using sqlite3.
        'NAME': 'csgointl',
        'USER': 'xzj',
        'PASSWORD': 'xzj2016',
        'HOST': '172.16.20.70',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',  # Set to empty string for default.
    },
    'slave': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'csgointl',  # Or path to database file if using sqlite3.
        'USER': 'xzj',
        'PASSWORD': 'xzj2016',
        'HOST': '172.16.20.70',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',  # Set to empty string for default.
    },
    'bots': {
        'ENGINE': 'sql_server.pyodbc',
        # 'HOST': '119.29.67.227', 外网
        # 'HOST': '10.251.220.137', 内网
        # 'PORT': '4994',
        'NAME': 'SteamData_test',
        'USER': 'testonly',
        'PASSWORD': 'W#qoiAiCEOY0',
        'OPTIONS': {
            'host_is_server': True,
            'driver': 'ODBC Driver 11 for SQL Server',
            'dsn': 'STEAMDATA',
            'encoding': 'utf-8',
            'autocommit': True,
        }
    },

}
# MIDDLEWARE_CLASSES = (
#     'django.middleware.common.CommonMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.locale.LocaleMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
#     # Uncomment the next line for simple clickjacking protection:
#     # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
# )
##################################################################s
# Logging settings
##################################################################

OMONEY_IP_WHITE_LIST = ['172.16.12.38', '172.16.110.54', '127.0.0.1']

LOG_DATE_FORMAT = '%d %b %Y %H:%M:%S'

LOG_FORMATTER = logging.Formatter(
    u'%(asctime)s | %(levelname)-7s | %(name)s | %(message)s',
    datefmt=LOG_DATE_FORMAT)

CONSOLE_HANDLER = logging.StreamHandler()

CONSOLE_HANDLER.setFormatter(LOG_FORMATTER)

CONSOLE_HANDLER.setLevel(logging.DEBUG)

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt': "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#         'elk_json': {
#             'format': '%(message)s'
#         },
#     },
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         # 按日期存储
#         'file': {
#             'level': 'ERROR',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'when': 'midnight',
#             'backupCount': 0,
#             'filename': '/data/htdocs/dj-csgo/logs/django.log',
#             'formatter': 'verbose'
#         },
#         'bots_file': {
#             'level': 'INFO',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'when': 'midnight',
#             'backupCount': 0,
#             'filename': '/data/htdocs/dj-csgo/logs/bots.log',
#             'formatter': 'verbose'
#         },
#         'bots_callback_file': {
#             'level': 'INFO',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'when': 'midnight',
#             'backupCount': 0,
#             'filename': '/data/htdocs/dj-csgo/logs/bots_callback.log',
#             'formatter': 'verbose'
#         },
#         'steam_analyst_file': {
#             'level': 'INFO',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'when': 'midnight',
#             'backupCount': 0,
#             'filename': '/data/htdocs/dj-csgo/logs/steam_analyst.log',
#             'formatter': 'verbose'
#         },
#         'elk_bots_file': {
#             'level': 'INFO',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'when': 'midnight',
#             'backupCount': 0,
#             'filename': '/data/htdocs/dj-csgo/logs/elk_bots_json.log',
#             'formatter': 'elk_json'
#         },
#         'elk_pay_file': {
#             'level': 'INFO',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'when': 'midnight',
#             'backupCount': 0,
#             'filename': '/data/htdocs/dj-csgo/logs/elk_pay_json.log',
#             'formatter': 'elk_json'
#         },
#         'elk_wallet_file': {
#             'level': 'INFO',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'when': 'midnight',
#             'backupCount': 0,
#             'filename': '/data/htdocs/dj-csgo/logs/elk_wallet_json.log',
#             'formatter': 'elk_json'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'django_tools.DynamicSite': {
#             'handlers': ['console'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'bots': {
#             'handlers': ['bots_file'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#         'bots_callback': {
#             'handlers': ['bots_callback_file'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#         'steam_analyst': {
#             'handlers': ['steam_analyst_file'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#         'elk_bots': {
#             'handlers': ['elk_bots_file'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#         'elk_pay': {
#             'handlers': ['elk_pay_file'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#         'elk_wallet': {
#             'handlers': ['elk_wallet_file'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#     },
# }

##################################################################
# Installed apps
##################################################################

DEVELOPMENT_APPS = (
    'debug_toolbar',
)

INSTALLED_APPS = EXTERNAL_APPS + DEVELOPMENT_APPS + INTERNAL_APPS
# INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS
INTERNAL_IPS = ('127.0.0.1', '192.168.110.128','172.16.12.23')
DEBUG_TOOLBAR_CONFIG = {
    # Toolbar options
    # 'INTERCEPT_REDIRECTS': False,
    # 'JQUERY_URL': 'http://libs.useso.com/js/jquery/1.11.1/jquery.min.js'
    'JQUERY_URL': '/static/csgo/js/jquery.js'
}
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://172.16.20.141:6379/6",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

REDIS_IP = "172.16.20.141"
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://119.29.100.124:6379/2",  # 2.0版本用db2
#         "LOCATION": "redis://101.200.85.129:6379/2",  # 2.0版本用db2
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
#     'E:/gt/dj-front-end/static',
# )
# MS_STATIC_URL = '/static/www.fifacoinsland.com/'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
            PROJECT_DIR / 'templates',
        ],
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'dj_csgo.context_processors.multi_site_static',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                # insert your TEMPLATE_LOADERS here
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 259200
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['console'],
#             'propagate': True,
#             'level': 'DEBUG',
#         },
#     }
# }
LOGGING.get('handlers')['console'] = {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
LOGGING.get('loggers')['django.db.backends'] = {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        }
# sentry
# RAVEN_CONFIG = {
#     'dsn': 'http://a550fbdd05c640f6b97cab47ee292ae1:547507e78e254d6181329644f66ff54a@172.16.20.157:9000/2',
#     # If you are using git, you can also automatically configure the
#     # release based on the git info.
#     'release': 'test_logs',
# }

# RAVEN_CONFIG = {
#     'dsn': 'http://a08d6885175d411785b67c8c2f9606d7:5e839802c9c240b890191a85d1aa19f8@172.16.20.157:9000/4',
#     # If you are using git, you can also automatically configure the
#     # release based on the git info.
#     'release': 'testing_intl',
# }


# steam 认证回调 steam auth
ABSOLUTE_URL = 'csgo2.mmoxe.com:9090'
# 支付宝 支付接口地址
#API_URL = 'http://payment.igxe.com.cn/alipay/direct'
# 支付宝callback地址 igxe
#NOTIFY_URL = 'http://payment.igxe.com.cn/alipaRETURN_RULy/callback'
# 支付宝callback地址 csgo
#EXTRA_COMMON_PARAM = 'http://119.29.138.159:9090/alipay_callback'
# 支付宝callback csgo thanks page
#RETURN_RUL = 'http://csgo2.mmoxe.com:9090/pay_succ'
RETURN_RUL = 'http://172.16.12.38:8000/pay_done'
# 充值成功回调页面
RECHARGE_RETURN_RUL = 'http://csgo2.mmoxe.com:9090/recharge_succ'
# 订单号前缀
ORDER_NUMBER_PREF = 'CSGODEV'
# 充值订单前缀
RECHARGE_PREF = 'CSGODEVCHARGE'
# 404
handler404 = "dj_csgo.views.redirect_page_not_found"
# 机器人2.0取回回调地址
BOTS2_FETCH_CALL_BACK_URL = 'http://172.16.12.23:8000/bots2_fetch_callback'
# 机器人2.0上架回调地址
BOTS2_SALE_CALL_BACK_URL = 'http://172.16.12.23:8000/bots2_sale_callback'
# 机器人2.0交易地址
BOTS2_TRADE_URL = 'http://172.16.14.65:8082/product/trade'
# 机器人2.0获取库存报文地址
BOTS2_INVENTORY_URL = 'http://172.16.14.65:8083/stock/query/where'
# ip白名单
IP_WHITE_LIST = ['172.16.14.65', '119.29.147.221', '172.16.14.85', '172.16.20.174', '172.16.12.38', '172.16.20.116']
# 支付2.0回调地址
PAY_CALLBACK = 'http://172.16.12.38:8000/pay/callback'
# 充值调地址
RECHARGE_CALLBACK = 'http://172.16.12.23:8000/recharge/callback'
# 支付宝2.0请求地址
#PAY_ALI_URL = 'http://172.16.20.174:8090/alipay/alipay/alipayrequest'
# 微信支付 请求地址
#PAY_WX_URL = 'http://172.16.20.174:8090/wxpay/softIsland/generateErCode'
# 支付请求公共地址
PAY_URL = 'http://payment.mmoxe.com:9090/comonpay/softIsland/requestPay'
# 支付平台发送请求签名key
PAY_KEY_SEND = 'jzxFoeJAkcm5YK36aI5PvznWAYvt1Ne2'
# 支付平台回调签名key
PAY_KEY_BACK = 'QZHi4VUgqo9Vr1oaqI05xq1a88MmHVnh'

#PAYPAL_POST_URL = 'https://www.sandbox.paypal.com/cgi-bin/webscr'


# Paypal 支付
PAYPAL_PAYMENT_LOGIN_SUCCESS_URL = 'http://172.16.12.38:8000/loginPaypalPayCallBack'
#用户支付成功后台通知前端地址
PAYPAL_PAYMENT_NOTIFY_URL = 'http://172.16.12.38:8000/PaypalPaymentCallBack'
#用户发起退款后台通知前端地址
PAYPAL_PAYMENT_REFUNDING_URL = 'http://172.16.12.38:8000/PaypalPaymentRefund'
#用户退款结束后台通知前端地址
PAYPAL_PAYMENT_REFUNDED_URL = 'http://172.16.12.38:8000/PaypalPaymentRefund'
#用户支付中后台通知前端地址
PAYPAL_PAYMENT_PENDING_URL = 'http://172.16.12.38:8000/PaypalPaymentCallBack'

#龙通宝
#url
OMONEY_DOMAIN = 'http://test.omoney.com:8300'
OMONEY_CLIENT_ID = 'ruandao_client'
OMONEY_CLIENT_SECRET = 'ruandao_secret'


PAYPAL_IP_WHITE_LIST = ['172.16.20.116', '172.16.20.116', '127.0.0.1', '172.16.12.38']
#回调页面地址
OMONEY_CHARGE_RETURN_URL = 'http://172.16.12.38:8000/cashout/bankinfo'
#支付回调地址
OMONEY_CHARGE_NOTIFY_URL = 'http://172.16.12.38:8000/chargeOmoneyCallBack'
#PAYPAL支付
PAYPAL_API_URL = 'http://172.16.12.38:8080/softIsland/payPalRequest'
# paypal 充值前登陆请求地址
PAYPAL_LOGIN_URL = 'http://172.16.20.116:8090/paypal/softIsland/payPalNvpLogin'
# 获取paypal账户信息
PAYPAL_ACCOUNT_URL = 'http://172.16.20.116:8090/paypal/softIsland/payPalNvpVerify'
# paypal 请求支付地址
PAYPAL_REAL_PAY_URL = 'http://172.16.20.116:8090/paypal/softIsland/payPalNvpPay'
# paypal登陆成功后页面
PAYPAL_LOGIN_SUCCESS_URL = 'http://172.16.12.38:8000/loginPaypalCallBack'
#支付成功后页面地址
PAYPAL_CHARGE_SUCCESS_URL = 'http://172.16.12.38:8000/charge_done'
#支付时用户取消支付后跳转地址
PAYPAL_CHARGE_CANCEL_URL = 'http://172.16.12.38:8000/charge_failed'
#用户支付成功后台通知前端地址
PAYPAL_CHARGE_NOTIFY_URL = 'http://172.16.12.38:8000/chargPaypalCallBack'
#用户发起退款后台通知前端地址
PAYPAL_CHARGE_REFUNDING_URL = 'http://172.16.12.38:8000/RefundPaypalCallBack'
#用户退款结束后台通知前端地址
PAYPAL_CHARGE_REFUNDED_URL = 'http://172.16.12.38:8000/RefundSuccPaypalCallBack'
#用户支付中后台通知前端地址
PAYPAL_CHARGE_PENDING_URL = 'http://172.16.12.38:8000/chargPaypalCallBack'
#支付的MD5码
PAYPAL_CHARGE_SENDSIGN = 'jzxFoeJAkcm5YK36aI5PvznWAYvt1Ne2'
#回调的MD5码
PAYPAL_CHARGE_RETURNSIGN = 'QZHi4VUgqo9Vr1oaqI05xq1a88MmHVnh'


# G2A url'
G2A_API_URL = 'http://172.16.20.116:8090/g2apay/softIsland/g2aPayRequest'
G2A_PAYMENT_SUCCESS_URL = 'http://172.16.12.38:8000/pay_succ'
G2A_PAYMENT_FAIL_URL = 'http://172.16.12.38:8000/pay_failed'
G2A_PAYMENT_NOTIFY_URL = 'http://172.16.12.38:8000/gta_payment_callback'

G2A_CHARGE_SUCCESS_URL = 'http://172.16.12.38:8000/charge_done'
G2A_CHARGE_CANCEL_URL = 'http://172.16.12.38:8000/charge_failed'
G2A_CHARGE_NOTIFY_URL = 'http://172.16.12.38:8000/gta_charge_callback'
G2A_IP_WHITE_LIST = ['172.16.20.116', '172.16.20.174', '127.0.0.1', '172.16.12.38']
G2A_MD5_SEND_SIGN = PAYPAL_CHARGE_SENDSIGN
G2A_MD5_RETURN_SIGN = PAYPAL_CHARGE_RETURNSIGN

# bitcoin
BITCOIN_API_URL = 'http://172.16.20.116:8090/bitcoinpay/softIsland/bitcoinPayRequest'
BITCOIN_CHARGE_SUCCESS_URL = 'http://172.16.12.38:8000/bitcoin_charge_done'
BITCOIN_CHARGE_NOTIFY_URL = 'http://172.16.12.38:8000/bitcoin_charge_callback'
BITCOIN_MD5_SEND_SIGN = 'jzxFoeJAkcm5YK36aI5PvznWAYvt1Ne2'
BITCOIN_MD5_RETURN_SIGN = 'QZHi4VUgqo9Vr1oaqI05xq1a88MmHVnh'

#亚马逊BOTO3
BOTO3_KEY = 'AKIAJTMHK42I74N6WJTA'
BOTO3_SECRET = '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'
BOTO3_BUCKET = 'csgoskin'

# # thrift接口端口
THRIFT_API_IP = '172.16.14.83'
# THRIFT_API_PORT = 9020
THRIFT_API_PORT = 6655

# 代理商提现比例，计算代理商可以得到的金额
AFFILIATE_WITHDRAW_COMMISSION = 0.005

# 收取国际卖家的手续费0.07
PLATFORM_FEE_RATE = 0.08

# 消息中间件异步接口地址
SEND_ASYN_MESSAGE_URL = 'http://172.16.16.42:8082/softisland/message/send/asyn'
# 消息中间件同步步接口地址
SEND_SYNC_MESSAGE_URL = 'http://172.16.16.42:8082/softisland/message/send/sync'
#发出消息站点
FROM_SITE_ID = "2"
#接受消息站点
REVICE_SITE_ID = "1"

TIME_ZONE = 'Asia/Shanghai'

# 美元货币
USD_CURRENCY = 1
# 巴西货币
BRL_CURRENCY = 5

ES_HOST = '172.16.20.141'
ES_PORT = 9200

ES_CONFIG = [
    {'host': '172.16.20.142', 'port': 9200},
    {'host': '172.16.20.141', 'port': 9200},
]

BROKER_URL = 'redis://172.16.20.141:6379/7'

UCENTER_URL = 'http://172.16.14.44/{uri}'
UCENTER_CLIENT_CODE = '11BFB293F471A1A7ABB1A7A57CCE263B'
UCENTER_SIGNATURE_CODE = 'softisland'


ACTIVITY_GIFTS_STEAM_UID = 76561198319213522
GOOD_GIFTS_STEAM_UID = 76561198318711909
ACTIVITY_EVERYDAY_TIMES_ADD = 3
ACTIVITY_FIRST_CHARGE_TIMES_ADD = 5
ACTIVITY_BEGIN_TIME = '2016-12-22'

FACEBOOK_SHARE_APPID = 148319082314272

SYNTHETICAL_PAY_SUCCESS = 'http://172.16.20.113/pay/success'
SYNTHETICAL_PAY_FAIL = 'http://172.16.20.113/pay/fail'
SYNTHETICAL_ADD_FUND = 'http://172.16.20.113/userCenter/payment/addfunds'
