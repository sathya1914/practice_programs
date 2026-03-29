'''INSTALL Packges:
    
1.The pip package manager:
    pip an acronym PIP Installs package,interacts with the python package index
    (PyPI), a massive repository of open-source software. it handles the downloading,
    installing and dependency resolution of Python packages.

    Ket Features:
    Dependency Resolution: if package A requires package B,PIP automatically installs
    both.
    version control:allows you to specify which version of library your code needs
    ecosystem standard:it becomes pre-installed with most python distribution.



2.installing packages:
    Tip:use virtual environment
    use should never install packages to your global python environment,always use a virtual
    environment to support project dependence



    open cmd:
    #create a virtual environment : python -m env env

    #activate it:  .\venv\Script\activate

    #basic installation:  pip install requests


    #Installing pckages:  pip install pandas

    #install specific version:  pip install pandas=2.1.0

    #upgrade an existing pacckage:  pip install --upgrade numpy
    
    
####what pip does internally:


    connects to PyPI
    download requests
    check what other packages requests needs
    install all of them in correct order
    make them available to your python code

#depency resolution

   your code--->Flask
   Flask--->needs werkzueg
   Werkzueng--->needs MarkupSafe

   when you install one thing,pip install everythng needed

3.unistalling packages:
      pip uninstall pandas
      when promted proceed(y/n)? you must type y.
      pip unistall -y pandas (auto confirmation).

4.the requirements.txt file:

    creating the file:
    pip freeze>requirementsfile.txt

    install pacakges specified in file:
    pip install -r requirementsfile.txt'''
