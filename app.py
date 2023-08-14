from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


# Configuración de la base de datos

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:password@localhost:3306/sentinel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de la tabla "usuarios"
#class usuarios(db.Model):
 #   id_usuario = db.Column(db.Integer, primary_key=True)
  #  id_tarjeta = db.Column(db.String(20))
   # nombre_usuario = db.Column(db.String(100))

# Definir el modelo Registro_acceso
class associations(db.Model):
    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.Integer)
    state = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    
    
class records(db.Model):
    id = db.Column(db.Integer,autoincrement = True, primary_key=True)
    assoc_id = db.Column(db.String, db.ForeignKey('associations.id'))
    date = db.Column(db.DateTime)

# Variable global para almacenar la última id_tarjeta recibida
mi_variable_global = None


mi_variable_global2 =  None



# Ruta para obtener los IDs y nombres de las tarjetas
@app.route('/tarjetas', methods=['GET'])
def get_tarjetas_ids_nombres():
    usuarios_lista = associations.query.all()
    resultado = [{"id": usuario.id} for usuario in usuarios_lista]
    return jsonify(resultado)

# Ruta para crear un registro de acceso en la base de datos
@app.route('/registro_acceso', methods=['POST'])
def crear_registro():
    data = request.get_json(force=True)
    assoc_id = data['assoc_id']
    #fecha_hora = data['fecha_hora']
    
    nuevo_acceso_registro = records(assoc_id =assoc_id)
    
    db.session.add( nuevo_acceso_registro )
    db.session.commit()
     
    return jsonify({"mensaje": "Registro creado exitosamente"})

# Ruta para recibir la variable y almacenarla en la aplicación
@app.route('/enviar_variable', methods=['POST'])
def enviar_variable():
    data = request.json
    global mi_variable_global
    mi_variable_global = data.get('id_tarjeta')
    
    return {'message': 'Variable recibida y almacenada correctamente'}

# Ruta para mostrar la variable en una página web
@app.route('/')
def LISTA():
    usuarios_lista = records.query.all()
    resultado = [{"id": usuario.id} for usuario in usuarios_lista]
    
    return render_template('index.php', variable=resultado)

@app.route('/form')
def mostrar_variable():
    global mi_variable_global
    variable = mi_variable_global
    return render_template('create.php')


#class Association(db.Model):
#    id = db.Column(db.String(255), nullable=False)
#    user_id = db.Column(db.Integer, primary_key=True)  
#   state = db.Column(db.Integer, nullable=False)


@app.route('/enviar', methods=['POST'])
def relacion():
    #data = request.json
    
    id = request.form.get('rfid')
    user_id = request.form.get('id')    
    state = 1
    new_association = associations(id=id, user_id=user_id, state=state)
    db.session.add(new_association)
    db.session.commit()



























@app.route('/conexion')
def formeeee():
    
    return render_template('conexion.php')

if __name__ == "__main__":
    app.run(debug=True)

