from loguru import logger
from sys import stderr



logger.add("meu_log.log", level="CRITICAL")

def soma(x, y):
    try:
        soma = x + y
        logger.info(f'voce digitou valores corretos, parabens {soma}')
        return soma
    except:
        logger.critical("Voce precisa digitar valores corretos")

print(soma(2,3))
print(soma(2,7))
print(soma(2,"3"))
