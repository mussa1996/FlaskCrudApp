from flask import (
    Flask,
    render_template,
    redirect,
    flash,
    request,
    url_for,
    session
)

from datetime import timedelta
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    DatabaseError,
    InterfaceError,
    InvalidRequestError,
)
from werkzeug.routing import BuildError
from App import create_app,db
from Models import Employee
from dotenv import load_dotenv
app = Flask(__name__)
app.secret_key = '!secret'
app = create_app()

@app.route('/')
def index():
    all_data = Employee.query.all()
    
    return render_template('index.html',employees=all_data)

@app.route('/insert', methods=['POST'])
def  insert():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            emp = Employee(name=name,email=email,phone=phone)
            db.session.add(emp)
            db.session.commit()
            flash('Employee Added Successfully')
            return redirect(url_for('index'))
        except IntegrityError as e:
            db.session.rollback()
            flash('Employee Already Exists')
            return redirect(url_for('index'))
        except DataError as e:
            db.session.rollback()
            flash('Invalid Data')
            return redirect(url_for('index'))
        except DatabaseError as e:
            db.session.rollback()
            flash('Database Error')
            return redirect(url_for('index'))
        except InterfaceError as e:
            db.session.rollback()
            flash('Interface Error')
            return redirect(url_for('index'))
        except InvalidRequestError as e:
            db.session.rollback()
            flash('Invalid Request')
            return redirect(url_for('index'))
        except BuildError as e:
            db.session.rollback()
            flash('Build Error')
            return redirect(url_for('index'))
@app.route('/update', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        try:
            id = request.form['id']
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            emp = Employee.query.filter_by(id=id).first()
            emp.name = name
            emp.email = email
            emp.phone = phone
            db.session.commit()
            flash('Employee Updated Successfully')
            return redirect(url_for('index'))
        except IntegrityError as e:
            db.session.rollback()
            flash('Employee Already Exists')
            return redirect(url_for('index'))
        except DataError as e:
            db.session.rollback()
            flash('Invalid Data')
            return redirect(url_for('index'))
        except DatabaseError as e:
            db.session.rollback()
            flash('Database Error')
            return redirect(url_for('index'))
        except InterfaceError as e:
            db.session.rollback()
            flash('Interface Error')
            return redirect(url_for('index'))
        except InvalidRequestError as e:
            db.session.rollback()
            flash('Invalid Request')
            return redirect(url_for('index'))
        except BuildError as e:
            db.session.rollback()
            flash('Build Error')
            return redirect(url_for('index'))
@app.route('/delete/<id>/', methods=['GET','POST'])
def delete(id):
    my_data = Employee.query.filter_by(id=id).first()
    db.session.delete(my_data)
    db.session.commit()
    flash('Employee Deleted Successfully')
    return redirect(url_for('index'))
    

if __name__ == "__main__":
    app.run(debug=True)
    
    

