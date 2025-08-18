from config import settings
import sys
import platform

def create_allure_environment_file():
    # Сбор данных из settings и дополнительной информации об окружении
    environment_info = {
        **settings.model_dump(),
        "os_info": f"{platform.system()}, {platform.release()}",
        "python_version": sys.version
    }

    # Формируем строки вида key=value
    properties = '\n'.join([f'{key}={value}' for key, value in environment_info.items()])

    # Записываем в файл environment.properties в указанной директории
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)