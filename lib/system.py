import psutil


class System:
    def get_all():
        data = {
            "CPU": {
                "cores": CPU.get_count(),
                "percent": CPU.get_percent()
            },
            "SWAP": {
                "percent": SWAP.get_percent(),
                "available": SWAP.get_available(),
                "used": SWAP.get_used(),
                "total": SWAP.get_total()
            },
            "MEMORY": {
                "percent": MEMORY.get_percent(),
                "available": MEMORY.get_available(),
                "used": MEMORY.get_used(),
                "total": MEMORY.get_total()
            },
            "DISK": {
                "percent": DISK.get_percent(),
                "available": DISK.get_available(),
                "used": DISK.get_used(),
                "total": DISK.get_total()
            }
        }

        return data


class CPU:
    def get_count():
        return psutil.cpu_count(logical=False)

    def get_percent():
        return psutil.cpu_percent(4)


class SWAP:
    def get_percent():
        return psutil.swap_memory().percent

    def get_available():
        return psutil.swap_memory().free

    def get_used():
        return psutil.swap_memory().used

    def get_total():
        return psutil.swap_memory().total


class MEMORY:
    def get_percent():
        return psutil.virtual_memory().percent

    def get_available():
        return psutil.virtual_memory().available

    def get_used():
        return psutil.virtual_memory().used

    def get_total():
        return psutil.virtual_memory().total


class DISK:
    def get_percent():
        return psutil.disk_usage('/').percent

    def get_available():
        return psutil.disk_usage('/').free

    def get_used():
        return psutil.disk_usage('/').used

    def get_total():
        return psutil.disk_usage('/').total
