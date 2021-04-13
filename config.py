class mqtt:
    broker="broker.emqx.io"
    port=1883
    timeout=60

# 设备提供的能力
capability = {
    "cpu_usage_rate":"cpu 使用率",
    "cpu_temp":"CPU 温度",
    "memery_total":"内存总量",
    "memery_usage_rate":"内存使用率",
    "sd_total":"sd卡总容量",
    "sd_usage_rate":"sd卡使用率",
    "eth1_input":"网卡1上行带宽",
    "eth1_output":"网卡下行带宽",
}
