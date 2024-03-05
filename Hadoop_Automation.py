import os

# ------------->>   To Install Hadoop on the system <<-------


def install_hadoop():
    pre = input("Do you have the hadoop rpm downloaded already?(y/n): ")
    if(pre == "n"):
        print("Can't he;p you directly")
    else:
        y = input("Input the full-directory where rpm is downloaded/saved")
        os.system(y)
        os.system("yum install -y java-1.8.0-openjdk")
        os.system("rpm -ivh hadoop-1.2.1-1.x86_64 --force")

# ------------->>   To create a namenode on hadoop  <<-------


def create_namenode_hadoop():
    os.system("hadoop namenode -format")
    os.system("cd /etc/hadoop")
    os.system("rm -rf hdfs-site.xml")
    os.system("rm -rf core-site.xml")
    ipm = input("Input master IP: ")
    dir2 = input("Name your directory you want to create and use: ")
    os.system("mkdir /"+dir2)
    os.system("cd /etc/hadoop")
    f2 = open("/etc/hadoop/hdfs-site.xml", "w")
    f2.write('''
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.name.dir</name>
<value>/{}</value>
</property>
</configuration>'''.format(dir2))
    f2.close()
    os.system("systemctl disable firewalld")
    os.system("systemctl stop firewalld")
    f3 = open("/etc/hadoop/core-site.xml", "w")
    f3.write("""
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}</value>

</property>
</configuration>""".format(ipm))
    f3.close()
    os.system("hadoop-daemon.sh start namenode")





# ------------->>   To create a datanode on hadoop  <<-------

def create_datanode_hadoop():
    os.system("cd /etc/hadoop")
    os.system("rm -rf hdfs-site.xml")
    os.system("rm -rf core-site.xml")
    dir2 = input("Name your directory you want to create and use: ")
    os.system("mkdir /"+dir2)
    ipm = input("Please enter the Ip of master You want to connect with: ")
    f4 = open("/etc/hadoop/hdfs-site.xml", "w")
    f4.write('''
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{}</value>
</property>
</configuration>'''.format(dir2))
    f4.close()
    f5 = open("/etc/hadoop/core-site.xml", "w")
    f5.write("""
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}</value>

</property>
</configuration>""".format(ipm))
    f5.close()
    os.system("systemctl disable firewalld")
    os.system("systemctl stop firewalld")
    os.system("hadoop-daemon.sh start datanode")


# ------------->>   To create a client on hadoop    <<-------

def create_hadoop_client():
    os.system("systemctl stop firewalld")
    os.system("systemctl disable firewalld")
    ipm = input("Please enter the Ip of master You want to connect with: ")
    f5 = open("/etc/hadoop/core-site.xml", "w")
    f5.write('''
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}</value>

</property>
</configuration>'''.format(ipm))
    f5.close()

