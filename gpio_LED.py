#引入需要用到的硬件库
import utime
from Maix import GPIO
from fpioa_manager import fm

#自定义引脚名称
io_led_g = 12
io_led_r = 13
io_led_b = 14

#注册外设资源到某个具体的引脚
fm.register(io_led_r,fm.fpioa.GPIO0)

#定义一个GPIO对象并设置工作模式
led_r=GPIO(GPIO.GPIO0,GPIO.OUT)

while(1):
    led_r.value(0)#io口输出低电平
    utime.sleep_ms(500)
    led_r.value(1)#io口输出高电平
    utime.sleep_ms(500)
