# GetNote
<<<<<<< HEAD

### 📖 Install

```
$ git clone https://github.com/ycv005/getnote.git
$ cd getnote
$ pipenv install
$ pipenv shell

# Run Migrations
$ python manage.py migrate

# Create a Superuser:
$ python manage.py createsuperuser

# Confirm everything is working:
$ python manage.py runserver

# Load the site at http://127.0.0.1:8000
```

=======
(Optional) First of all, [Install Virtual Env](https://pypi.org/project/virtualenv/)
</br>
(Optional) Creating Virtual Env(venv_getnote is my venv name, choose your acc.)-
`python -m venv venv_getnote` 
</br></br>
Install django- `pip install django`
</br></br>
Command to Activate the Virtual env-</br></br>
For Linux Environment-</br>
 `. venv_getnote/bin/activate` (my virtual env name- venv_getnote)</br></br>
For Windows & [Git Bash on Window](https://git-scm.com/download/win)-</br>
`venv_getnote\Scripts\activate`
</br></br>
For Mac-</br>
`. venv_getnote/bin/activate` or `venv_getnote myvenv/bin/activate`
</br></br>
To Run django Server- `python manage.py runserver`</br></br>
>>>>>>> parent of f250d27... Merge pull request #19 from ycv005/note
To Run the django Interactive interpreter (shell)- `python manage.py shell`</br></br>
Any changes to db/models, run following code</br>
```
python manage.py makemigrations
python manage.py migrate
```
</br></br>
Any changes to static files, we need to collect static files (as result your new files will be added to static folder)</br>
```
python manage.py collectstatic
```
</br></br>
To Know the work flow and progress, follow the branch in series
1. [Master](https://github.com/ycv005/getnote)- All the work will be merged to this branch.
2. [Accounts](https://github.com/ycv005/getnote/tree/accounts)- Works related to cookies based auth.
2. [Note](https://github.com/ycv005/getnote/tree/note)- Works related to Note.
