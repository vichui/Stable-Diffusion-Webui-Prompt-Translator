import launch

if not launch.is_installed("deep-translator"):
    launch.run_pip("install deep-translator", "requirement for google free")
