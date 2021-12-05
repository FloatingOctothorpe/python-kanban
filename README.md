Python Kanban Board
===================
A simple Kanban board application using [Flask][flask-home] and
[SQLite][sqlite-home].

Running locally
---------------
The application can be run with the following steps:

 1. Install required python packages:

        pip install -r requirements.txt

 __Note__: this will install packages globally, the [venv module][venv-docs]
 can be used to set up a virtual environment if you want to avoid changing the
 system packages.

 2. Run the application using `flask`:

        FLASK_APP=main.py flask run

 3. Finally connect to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in a
    web browser.

License
-------
With the exception of the following, all code in this repository is released
under the terms of the [GNU General Public License v3][gpl-v3]:

 * [plus][plus-icon] and [edit][edit-icon] icons were created by Andrian
   Valeanu, and are available under the [Creative Commons (CC BY-NC
   3.0)][cc-by-nc-3.0] license.
 * [Vue.js][vuejs-home] is released under the [MIT License][mit-license].

[cc-by-nc-3.0]: https://creativecommons.org/licenses/by-nc/3.0/
[edit-icon]: https://www.iconfinder.com/icons/103173/edit_new_write_icon
[flask-home]: http://flask.pocoo.org/
[gpl-v3]: https://www.gnu.org/licenses/gpl-3.0.en.html
[mit-license]: https://opensource.org/licenses/MIT
[plus-icon]: https://www.iconfinder.com/icons/103172/add_plus_icon
[sqlite-home]: https://www.sqlite.org/
[venv-docs]: https://docs.python.org/3/library/venv.html
[vuejs-home]: https://vuejs.org/
