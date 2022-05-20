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


class ModelFormItem(FlaskForm):
    grupo = StringField('Grupo', validators=[Length(min=4, max=20)])
    subgrupo = StringField('SubGrupo', validators=[Length(min=4, max=20)])
    nome = StringField('Nome', validators=[DataRequired(), Length(min=4, max=50)])
    descricao = StringField('Descrição', validators=[Length(min=4, max=150)])
    un = StringField('Un.Med.', validators=[Length(min=2, max=10)])
    tipo = SelectField('Tipo', 
        choices=[   ("PRODUTO", "PRODUTO"), 
                    ("SERVICO", "SERVICO")])
    codigointerno = StringField('Cód.Int', validators=[Length(min=4, max=20)])
    ean = StringField('EAN', validators=[Length(min=4, max=13)])
    dun = StringField('DUN', validators=[Length(min=4, max=14)])

    cor = StringField('Cor', validators=[Length(min=4, max=20)])
    tamanho = StringField('Tamanho', validators=[Length(max=10)])
    largura = StringField('Largura')
    altura = StringField('Altura')
    comprimento = StringField('Compr.')

    pesoliquido = StringField('Peso Liq.')
    pesobruto = StringField('Peso Br.')
    estoqueminino = StringField('Est.Min.')
    estoquemaximo = StringField('Est.Max.')
    leadtime = StringField('LeadTime')

    loteminino = StringField('Lote Min.')
    lotemaximo = StringField('Lote Max.')
    ncm = StringField('NCM', validators=[Length(min=4, max=20)])
    cest = StringField('CEST', validators=[Length(min=4, max=20)])
    classificacao = SelectField('Classificação', 
        choices=[   ("", "Escolha uma Classificação"),
                    (1, "[1] - Produto para Revenda"),
                    (2, "[2] - Produção Própria"),
                    (3, "[3] - Serviço Prestado"),
                    (4, "[4] - Uso e Consumo"),
                    (5, "[5] - Serviços Diversos"),
                    (9, "[9] - Ativo Imobilizado")])
    
    ativo = SelectField('Ativo', 
        choices=[   (1, "ATIVO"), 
                    (0, "INATIVO")])
    id = StringField('ID')
    id_company = SelectField('Company')