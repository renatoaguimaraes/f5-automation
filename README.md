# f5-automation
Automation scripts to F5 operations based on https://github.com/F5Networks/f5-common-python. The scripts support DevOps and operating based environments docker containers.

### Scope

* Virtual servers (list, add and remove)
* Pools (list, add and remove)
* Members (list, add and remove)

### Before run

Install python 2.7 

Install pip

```
Download https://bootstrap.pypa.io/get-pip.py

python get-pip.py
```

Install f5 library.

```
pip install f5-sdk
```

### Usage

#### Virtual Server
```
vs-ls.py 
```

```
vs-add.py 
```

```
vs-rm.py 
```

#### Pool

```
pool-ls.py 
```

```
pool-add.py 
```

```
pool-rm.py 
```

#### Member

```
member-ls.py 
```

```
member-add.py 
```

```
member-rm.py 
```



