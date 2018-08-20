import bot
import newcheck_cr
from multiprocessing import Process


p = Process(target = newcheck_cr.run_check)
p.start()

pipe = Pipe
bot.run_bot()
