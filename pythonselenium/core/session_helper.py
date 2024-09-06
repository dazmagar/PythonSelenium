from pythonselenium import config as ps_config


def end_reused_class_session_as_needed():
    if (
        hasattr(ps_config, "reuse_class_session")
        and ps_config.reuse_class_session
        and hasattr(ps_config, "shared_driver")
        and ps_config.shared_driver
    ):
        if (
            hasattr(ps_config.shared_driver, "service")
            and ps_config.shared_driver.service.process
        ):
            try:
                ps_config.shared_driver.quit()
            except Exception:
                ps_config.shared_driver = None
