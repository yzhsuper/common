# -*- coding: utf-8 -*-
import logging
import os
import sys

import djcelery
from path import path

djcelery.setup_loader()
##################################################################
# Application configuration
##################################################################

# The ID of the current site in the django_site database table.
SITE_ID = 1

# Directories
PROJECT_DIR = path(__file__).abspath().realpath().dirname().parent
PROJECT_NAME = PROJECT_DIR.basename()
SITE_DIR = PROJECT_DIR.parent
APPS_DIR = PROJECT_DIR / 'apps'
LIBS_DIR = PROJECT_DIR / 'libs'

# Append directories to sys.path
sys.path.append(SITE_DIR)
sys.path.append(APPS_DIR)
sys.path.append(LIBS_DIR)

# Root URLs module
ROOT_URLCONF = 'csgointl.urls'

# WSGI application
WSGI_APPLICATION = 'csgointl.wsgi.application'

##################################################################
# Language and timezone settings
##################################################################

# Specifies whether Django’s translation system should be enabled.
USE_I18N = True

# Specifies if localized formatting of data will be enabled by
# default or not.
USE_L10N = True

# Specifies if datetimes will be timezone-aware by default or not.
USE_TZ = False

# A string representing the time zone for this installation.
TIME_ZONE = 'America/Los_Angeles'

# A string representing the language code for this installation.
LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', u'en'),
    ('de', u'de'),
    ('pt', u'pt'),
    ('fr', u'fr'),
    ('ru', u'ru'),
    ('es', u'es'),
    # ('zh-hans', u'cn'),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, 'locale'),
)

FORMAT_MODULE_PATH = 'csgointl.formats'

##################################################################
# Authentication settings
################################################head##################

AUTH_USER_MODEL = 'steam_user.SteamUser'
AUTHENTICATION_BACKENDS = ('steam_user.djuserbackend.DJUserBackend',)

# The URL where requests are redirected for login.
LOGIN_URL = '/login/'

# The URL where requests are redirected for logout.
LOGOUT_URL = '/logout/'

# The URL where requests are redirected after login.
LOGIN_REDIRECT_URL = '/profile/'

##################################################################
# Middleware settings
##################################################################

# The default number of seconds to cache a page when the caching
# middleware or cache_page() decorator is used.
CACHE_MIDDLEWARE_SECONDS = 5

# The cache key prefix that the cache middleware should use.
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_NAME + '_'

# A tuple of middleware classes to use.
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'dj_csgo.middleware.DefenseMiddleware.Defense',
    'django.contrib.messages.middleware.MessageMiddleware',
    'dj_csgo.middleware.XForwardedForMiddleware.RealIP',
    'dj_csgo.middleware.SecretSessionMiddleware.OutBlack',
    'dj_csgo.middleware.SecretSessionMiddleware.Secret',
    # 'dj_csgo.middleware.ValidInfoMiddleware.Valid',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

##################################################################
# Static settings
##################################################################

# The absolute path to the directory where collectstatic will
# collect static files for deployment.
STATIC_ROOT = ''

# URL to use when referring to static files located in STATIC_ROOT.
STATIC_URL = '/static/'

# Additional locations the staticfiles app will traverse if the
# FileSystemFinder finder is enabled.
STATICFILES_DIRS = (
    PROJECT_DIR / 'static',
)

# The list of finder backends that know how to find static files
# in various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

##################################################################
# Templates settings
##################################################################

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

##################################################################
# Installed apps
##################################################################

EXTERNAL_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # Other external apps
)

INTERNAL_APPS = (
    # Application specific apps
    # 'dj_user',
    'geo',
    'dj_csgo',
    'steam_user',
    'exchange',
    'product',
    'cart',
    'order',
    'news',
    'wallet',
    'steam_analyst',
    'coupon',
    'bots',
    'alipay.create_direct_pay_by_user.dpn',
    'feedback',
    'raven.contrib.django.raven_compat',
    'nexus',
    'gargoyle',
    'thrift_client',
    'affiliate',
    'trade_synchro',
    'steamapi',
    'activity',
    'djcelery',
    'survey',
    'synthetical',
    'activity_draw',
    'unpack',
)

# openexchangerates.org service
# 免费key每月只能调用1000次
API_KEY_SETTINGS_KEY = '8127445a088549d59e5e1d7d8e1d161d'

# 开关配置
GARGOYLE_AUTO_CREATE = True

GARGOYLE_SWITCH_DEFAULTS = {
    # 加入购物车开关
    'cart_switch': {
        'is_active': True,
        'label': '购物车开关',
        'description': '关闭购物车用于升级,升级完成开放给公司ip测试',
    },
    # 支付宝支付开关
    'alipay_switch': {
        'is_active': True,
        'label': '支付宝支付开关',
    },
    # paypal支付开关
    'paypal_switch': {
        'is_active': True,
        'label': 'paypal支付开关',
    },
    # 龙通宝支付开关
    'omoney_switch': {
        'is_active': True,
        'label': '龙通宝支付开关',
    },
    # g2a支付开关
    'g2a_switch': {
        'is_active': True,
        'label': 'g2a支付开关',
    },
    # g2a支付开关
    'bitcoin_switch': {
        'is_active': True,
        'label': 'bitcoin支付开关',
    },
    # 钱包支付开关
    'wallet_switch': {
        'is_active': True,
        'label': '钱包支付开关',
    },
    # 上架开关
    'putaway_switch': {
        'is_active': True,
        'label': '上架开关',
        'description': '打开关闭上架功能',
    },
    # 取回开关
    'fetch_back_switch': {
        'is_active': True,
        'label': '取回开关',
        'description': '打开关闭所有取回操作',
    },
    # 高级开关
    'advanced_search_switch': {
        'is_active': True,
        'label': '高级搜索开关',
        'description': '关闭高级搜索可以应对cc攻击,提高服务器性能',
    },
    # 提现开关
    'cash_out_switch': {
        'is_active': True,
        'label': '提现开关',
        'description': '打开关闭提现功能',
    },
    # 监视地址开关
    'actions_link_switch': {
        'is_active': True,
        'label': '监视地址开关',
        'description': '打开关闭监视地址展示方式功能',
    },
    # 高级搜索登录开关
    'advanced_search_login_switch': {
        'is_active': True,
        'label': '高级搜索登录开关',
        'description': '打开关闭高级搜索登录功能',
    },
    # 限制用户不同ip，不同浏览器登录
    'session_key_switch': {
        'is_active': True,
        'label': '限制用户不同ip，不同浏览器登录',
        'description': '打开关闭限制用户不同ip，不同浏览器登录',
    },
    # 用户登录防御开关
    'defense_key_switch': {
        'is_active': True,
        'label': '用户登录防御开关',
        'description': '用户登录防御开关',
    },
    # 价格查询防御开关
    'query_price_key_switch': {
        'is_active': True,
        'label': '价格查询防御开关',
        'description': '价格查询防御开关',
    },
    # Elastic开关
    'es_search_switch': {
        'is_active': False,
        'label': 'Elastic开关',
        'description': '是否启用Elastic搜索',
    },
    # 是否同步交易信息到Elastic
    'product_trade_index_sync': {
        'is_active': False,
        'label': '同步索引开关',
        'description': '是否同步交易信息到Elastic',
    },
    # 钱包功能开关
    'access_wallet_switch': {
        'is_active': True,
        'label': '钱包功能开关',
        'description': '是否进行与钱包相关的功能',
    },
}

# steam收费api接口
# 接口需要指定ip才能调用，需要变更ip 找雷剑锋
API_KEY_STEAM_ANALYST = '1qjFJJCuPA70QUjtk'

# 日志
##################################################################
# Logging settings
##################################################################

LOG_DATE_FORMAT = '%d %b %Y %H:%M:%S'

LOG_FORMATTER = logging.Formatter(
    u'%(asctime)s | %(levelname)-7s | %(name)s | %(message)s',
    datefmt=LOG_DATE_FORMAT)

CONSOLE_HANDLER = logging.StreamHandler()

CONSOLE_HANDLER.setFormatter(LOG_FORMATTER)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(funcName)s] %(message)s\n",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s\n'
        },
        'elk_json': {
            'format': '%(message)s\n'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # 按日期存储
        'file': {
            'level': 'ERROR',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1000,
            'backupCount': 10,
            'delay': True,
            'filename': '/data/htdocs/csgointl/logs/django.log',
            'formatter': 'verbose'
        },
        'bots_file': {
            'level': 'INFO',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1000,
            'backupCount': 10,
            'delay': True,
            'filename': '/data/htdocs/csgointl/logs/bots.log',
            'formatter': 'verbose'
        },
        'bots_callback_file': {
            'level': 'INFO',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1000,
            'backupCount': 10,
            'delay': True,
            'filename': '/data/htdocs/csgointl/logs/bots_callback.log',
            'formatter': 'verbose'
        },
        'steam_analyst_file': {
            'level': 'INFO',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1000,
            'backupCount': 10,
            'delay': True,
            'filename': '/data/htdocs/csgointl/logs/steam_analyst.log',
            'formatter': 'verbose'
        },
        'elk_bots_file': {
            'level': 'INFO',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1000,
            'backupCount': 10,
            'delay': True,
            'filename': '/data/htdocs/csgointl/logs/elk_bots_json.log',
            'formatter': 'elk_json'
        },
        'elk_pay_file': {
            'level': 'INFO',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1000,
            'backupCount': 10,
            'delay': True,
            'filename': '/data/htdocs/csgointl/logs/elk_pay_json.log',
            'formatter': 'elk_json'
        },
        'elk_wallet_file': {
            'level': 'INFO',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1000,
            'backupCount': 10,
            'delay': True,
            'filename': '/data/htdocs/csgointl/logs/elk_wallet_json.log',
            'formatter': 'verbose'
        },
        'elk_thrift_file': {
            'level': 'INFO',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1000,
            'backupCount': 10,
            'delay': True,
            'filename': '/data/htdocs/csgointl/logs/elk_thrift_json.log',
            'formatter': 'verbose'
        },
        'elk_omoney_file': {
            'level': 'INFO',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1000,
            'backupCount': 10,
            'delay': True,
            'filename': '/data/htdocs/csgointl/logs/elk_omoney_json.log',
            'formatter': 'verbose'
        },
        'elk_aws_file': {
            'level': 'INFO',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1000,
            'backupCount': 10,
            'delay': True,
            'filename': '/data/htdocs/csgointl/logs/aws.log',
            'formatter': 'elk_json'
        },
        'elk_paypal_file': {
            'level': 'INFO',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1000,
            'backupCount': 10,
            'delay': True,
            'filename': '/data/htdocs/csgointl/logs/paypal.log',
            'formatter': 'elk_json'
        },
        'elk_syn_recive_file': {
            'level': 'INFO',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1000,
            'backupCount': 10,
            'delay': True,
            'filename': '/data/htdocs/csgointl/logs/elk_syn_recive.log',
            'formatter': 'elk_json'
        },
        'elk_order_file': {
            'level': 'INFO',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1000,
            'backupCount': 10,
            'delay': True,
            'filename': '/data/htdocs/csgointl/logs/elk_order.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django_tools.DynamicSite': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'bots': {
            'handlers': ['bots_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'bots_callback': {
            'handlers': ['bots_callback_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'steam_analyst': {
            'handlers': ['steam_analyst_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'elk_bots': {
            'handlers': ['elk_bots_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'elk_pay': {
            'handlers': ['elk_pay_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'elk_wallet': {
            'handlers': ['elk_wallet_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'elk_thrift': {
            'handlers': ['elk_thrift_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'elk_aws': {
            'handlers': ['elk_aws_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'elk_omoney': {
            'handlers': ['elk_omoney_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'elk_paypal': {
            'handlers': ['elk_paypal_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'elk_syn_recive': {
            'handlers': ['elk_syn_recive_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'elk_order': {
            'handlers': ['elk_order_file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# 美元货币
USD_CURRENCY = 1
# 巴西货币
BRL_CURRENCY = 5

# CN_BUYER_STEAM_UID = '76561198297428101'
# 国际站特殊steam 用户，国内货同步使用
INTL_SELLER_STEAM_UID = '76561198297428101'
# 同步接口盐值
MESSAGE_KEY = 'uMy4XPWdmqODSuuadhBwmn49qj8VVP'

# 溢价比例
PREMIUM_RATE = 0.05
