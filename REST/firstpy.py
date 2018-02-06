from eve import Eve
import psutil
import platform


app = Eve()


@app.route('/processor')
def processor():
    name = platform.processor()
    uname = platform.uname()
    sys = platform.system()
    ver = platform.version()

    s1 = []
    s1.append(" Operating System: "+str(sys))
    s1.append(" Processor: "+name)
    s1.append(" OS Version: "+ver)

    print(s1)
    return "<br>".join(s1)

@app.route('/ram')
def ram():
    mem = psutil.virtual_memory()
    print(mem)
    mem.total
    mem_gib = mem.total / (1024. ** 3)
    print(mem_gib)


    return "TOTAL RAM: "+str(mem_gib)+ " GB"

@app.route('/disk')
def disk():
    disk = psutil.disk_usage('/')
    disk_p = psutil.disk_partitions()

    print(disk_p)
    print(disk.total)
    return "Disk Usage: "+ str(disk)

if __name__ == '__main__':
    app.run()
