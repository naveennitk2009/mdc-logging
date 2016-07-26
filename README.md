# MDC Logging in Django/Python
``MDC logging`` now available in python. https://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/MDC.html

##Setup

1. Add to requirements file or simply add using pip

    `pip install git+ssh://git@github.com:grofers/mdc-logging.git`

2. Add to INSTALLED_APP if using django

    ```
    INSTALLED_APPS = [
        "mdc_logging",
    ]
    ```

2. Add logging formatter

    ```
    'formatters': {
            'mdc_formatter': {
                '()': 'mdc_logging.formatter.MDCFormatter'
            }
        }
    ```
    
    Add this formatter to logger handlers
    
##Usage

1. As a Middleware
    This can be used as middleware for logging request headers.
    Add these to settings.py of django project
    
    ```
    MIDDLEWARE_CLASSES = (
        "mdc_logging.middleware.MDCMiddleware",
    )
    ```
    
    ```
    HEADERS_TO_LOG = ["header_to_log_1", "header_to_log_2"]
    ```


2. Using as a module
    
    ```
    from mdc_logging.mdc import MDCLogging
    _mdc = MDCLogging()
    _mdc.set_mdc("new_message_key", "Hi I am new message key")
    logger.info("")
    ```

##Extending

In the next release will provide a way to extend formatter to log specific fields only.

##Running tests
```python runtests.py```
