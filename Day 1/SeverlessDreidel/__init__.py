import logging
import random

import azure.functions as func

dreidel = ["ג (Gimmel)","נ (Nun)","ה (Hay)","ש (Shin)"]

def roll_dreidel():
    rnd = random.randint(0,4)
    return dreidel[rnd]


def main(req: func.HttpRequest) -> func.HttpResponse:
    dreidel_str = roll_dreidel()

    return func.HttpResponse(f"You get {dreidel_str}!!")
