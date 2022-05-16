from flask import Flask, render_template, url_for, redirect, flash, session, request, jsonify
from conexao_mysql import *
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, DateTimeField, RadioField, BooleanField, PasswordField, 
                         SelectField, TextAreaField, DateField)
from wtforms.validators import DataRequired, InputRequired, Length


class ModelFormPeople(FlaskForm):
    grupo = StringField('Grupo', validators=[Length(min=4, max=20)])
    subgrupo = StringField('SubGrupo', validators=[Length(min=4, max=20)])
    nome = StringField('Nome', validators=[DataRequired(), Length(min=4, max=50)])
    razaosocial = StringField('Razão Social', validators=[Length(min=4, max=150)])
    tipo = SelectField('Tipo', 
        choices=[   ("JURIDICA", "PESSOA JURIDICA"), 
                    ("FISICA", "PESSOA FISICA")])
    cnpj = StringField('CNPJ', validators=[Length(min=4, max=20)])
    inscest = StringField('Insc.Est.', validators=[Length(min=4, max=20)])
    cpf = StringField('CPF', validators=[Length(min=4, max=11)])
    rg = StringField('RG', validators=[Length(min=4, max=11)])
    endereco = StringField('Endereço', validators=[Length(min=4, max=100)])
    
    numero = StringField('Num', validators=[Length(min=4, max=10)])
    complemento = StringField('Comp.', validators=[Length(min=4, max=20)])
    bairro = StringField('Bairro', validators=[Length(min=4, max=50)])
    cidade = StringField('Cidade', validators=[Length(min=4, max=50)])
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
    cep = StringField('CEP', validators=[Length(min=4, max=8)])
    telefone1 = StringField('Telefone1', validators=[Length(min=4, max=15)])
    telefone2 = StringField('Telefone2', validators=[Length(min=4, max=15)])
    email = StringField('Email', validators=[DataRequired(), Length(min=4, max=50)])
    id = StringField('ID')
    id_company = SelectField('Company')