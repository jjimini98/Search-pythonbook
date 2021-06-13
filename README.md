- [Project summary](#da-design-server)

  - [Purpose](#purpose)

  - [Requirements](#requirements)

  - [How to install](#how-to-install)

- [How to use](#how-to-use)

- [Version History](#version-history)

- [Contacts](#contacts)

- [License](#license)

---

### Project summary

#### Purpose

데이터아키텍처창의설계 수업 프로젝트 - server side

#### Requirements

* python >= 3.5.2

* flask >= 2.0.1
* mysql  Ver 15.1 Distrib 10.0.38-MariaDB, for debian-linux-gnu (x86_64) using readline 5.2
 

#### How to install

* Clone & Install

```sh

~$ git clone ...........

~$ cd DataArchitecture

~/DataArchitecture$pip3 install -r requirements.txt

```
* Append two lines below to '~/.bashrc' files.

```sh

~$ cat >> ~/.bashrc
export DATAARCHITECTURE=/root/DataArchitecture
export PYTHONPATH=$PYTHONPATH:$DATAARCHITECTURE

Ctrl+d

~$ source ~/.bashrc

```

---

### How to use

``` shell
~$ cd DataArchitecture/src/Server
~/DataArchitecture/src/Server$ python route.py 
```

- chrome, firefox 웹브라우저에서 ip주소와 5000번 포트번호를 입력하면 Pyinder에 접속이 가능 
* pip install로 모듈을 모두 설치했음에도 모듈이 import 되지 않는다면, 아래와 같이 실행해본다. 
```shell
apt-get install python-flask
apt-get install python-pymysql 
``` 


---

### Version History

* v.0.0.0 : 개발중

---

### Contacts

jjimini98@naver.com

---

### License

Apache-2.0


