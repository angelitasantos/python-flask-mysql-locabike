from flask import Flask, render_template, url_for, redirect, flash, session, request, jsonify
from conexao_mysql import *
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, DateTimeField, RadioField, BooleanField, PasswordField, 
                         SelectField, TextAreaField, DateField)
from wtforms.validators import DataRequired, InputRequired, Length


class ModelFormPeople(FlaskForm):
    grupo = StringField('Grupo')
    subgrupo = StringField('SubGrupo')
    nome = StringField('Nome', validators=[DataRequired(), Length(min=4, max=50)])
    razaosocial = StringField('Razão Social')
    tipo = SelectField('Tipo', 
        choices=[   ("JURIDICA", "PESSOA JURIDICA"), 
                    ("FISICA", "PESSOA FISICA")])
    cnpj = StringField('CNPJ')
    inscest = StringField('Insc.Est.')
    cpf = StringField('CPF')
    rg = StringField('RG')
    endereco = StringField('Endereço')
    
    numero = StringField('Num')
    complemento = StringField('Comp.')
    bairro = StringField('Bairro')
    cidade = StringField('Cidade')
    uf = SelectField('UF', 
        choices=[   ("", "Escolha um Estado"),
                    ("AC", "Acre"),
                    ("AL", "Alagoas"),
                    ("AP", "Amapá"),
                    ("AM", "Amazonas"),
                    ("BA", "Bahia"),
                    ("CE", "Ceará"),
                    ("DF", "Distrito Federal"),
                    ("ES", "Espírito Santo"),
                    ("GO", "Goiás"),
                    ("MA", "Maranhão"),
                    ("MT", "Mato Grosso"),
                    ("MS", "Mato Grosso do Sul"),
                    ("MG", "Minas Gerais"),
                    ("PA", "Pará"),
                    ("PB", "Paraíba"),
                    ("PR", "Paraná"),
                    ("PE", "Pernambuco"),
                    ("PI", "Piauí"),
                    ("RJ", "Rio de Janeiro"),
                    ("RN", "Rio Grande do Norte"),
                    ("RS", "Rio Grande do Sul"),
                    ("RO", "Rondônia"),
                    ("RR", "Roraima"),
                    ("SC", "Santa Catarina"),
                    ("SP", "São Paulo"),
                    ("SE", "Sergipe"),
                    ("TO", "Tocantins")])
    cep = StringField('CEP')
    telefone1 = StringField('Telefone1')
    telefone2 = StringField('Telefone2')
    email = StringField('Email', validators=[DataRequired()])
    id = StringField('ID')
    id_company = SelectField('Company')