from botcity.core import DesktopBot


# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


def not_found(label):
    print(f"Element not found: {label}")


class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        self.browse(
            "https://docs.google.com/forms/u/1/d/e/1FAIpQLSesJ6UCoKs6TCsMemPB1B_8m7IhN6-UYkwTG4nvL6lKxfh7ew"
            "/formResponse")

        if not self.find("encontrar", matching=0.97, waiting_time=10000):
            not_found("encontrar")
        if not self.find("funcionario", matching=0.97, waiting_time=10000):
            not_found("funcionario")
        self.click()
        self.paste('FUNCIONÁRIO')
        self.scroll_down(700)
        if not self.find("CPF", matching=0.97, waiting_time=10000):
            not_found("CPF")
        self.click()
        self.paste('210.210.210-59')
        if not self.find("CORDENADOOR", matching=0.97, waiting_time=10000):
            not_found("CORDENADOOR")
        self.click()
        if not self.find("DENNIEL", matching=0.97, waiting_time=10000):
            not_found("DENNIEL")
        self.click()
        self.scroll_down(200)
        if not self.find("CARRO", matching=0.97, waiting_time=10000):
            not_found("CARRO")
        self.click()
        self.paste('Jeep Renegade - FLEX 2021/22')
        self.scroll_down(350)
        if not self.find("PLACA", matching=0.97, waiting_time=10000):
            not_found("PLACA")
        self.click()
        self.paste('PLACA12L3')
        if not self.find("LOCADO", matching=0.97, waiting_time=10000):
            not_found("LOCADO")
        self.click()
        if not self.find("HUAWEI", matching=0.97, waiting_time=10000):
            not_found("HUAWEI")
        self.click()
        self.scroll_down(980)
        if not self.find("PROJETO", matching=0.97, waiting_time=10000):
            not_found("PROJETO")
        self.click()
        self.scroll_down(980)

        if not self.find("ATIVIDADE", matching=0.97, waiting_time=10000):
            not_found("ATIVIDADE")
        self.click()

        if not self.find("ATIVIDAE INICIO", matching=0.97, waiting_time=10000):
            not_found("ATIVIDAE INICIO")
        self.click()

        if not self.find("KM", matching=0.97, waiting_time=10000):
            not_found("KM")
        self.click()
        self.paste('45')
        self.scroll_down(450)
        if not self.find("observacao", matching=0.97, waiting_time=10000):
            not_found("observacao")
        self.click()
        self.paste('...')

        if not self.find("final de semana", matching=0.97, waiting_time=10000):
            not_found("final de semana")
        self.click()
        self.scroll_down(1000)

        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )


if __name__ == '__main__':
    Bot.main()
