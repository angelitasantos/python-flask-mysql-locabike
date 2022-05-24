from flask import Flask, render_template, url_for, redirect, flash, session, request, jsonify
from conexao_mysql import *
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, DateTimeField, RadioField, BooleanField, PasswordField, IntegerField,
                        DecimalField, SelectField, TextAreaField, DateField, FileField)
from wtforms.validators import DataRequired, InputRequired, Length


class ModelFormPeople(FlaskForm):
    grupo = StringField('Grupo', validators=[Length(min=4, max=20)])
    subgrupo = StringField('SubGrupo', validators=[Length(min=4, max=20)])
    nome = StringField('Nome', validators=[DataRequired(), Length(min=4, max=50)])
    razaosocial = StringField('Razão Social', validators=[Length(min=4, max=150)])
    tipo = SelectField('Tipo', 
        choices=[   ("JURIDICA", "PESSOA JURIDICA"), 
                    ("FISICA", "PESSOA FISICA")])
    cnpj = StringField('CNPJ', validators=[Length(max=20)])
    inscest = StringField('Insc.Est.', validators=[Length(max=20)])
    cpf = StringField('CPF', validators=[Length(max=20)])
    rg = StringField('RG', validators=[Length(max=20)])
    endereco = StringField('Endereço', validators=[Length(min=4, max=100)])
    
    numero = StringField('Num', validators=[Length(max=10)])
    complemento = StringField('Comp.', validators=[Length(max=20)])
    bairro = StringField('Bairro', validators=[Length(min=4, max=50)])
    cidade = StringField('Cidade', validators=[Length(min=4, max=50)])
    uf = SelectField('UF', 
        choices=[   ("", "ESCOLHA UM ESTADO"),
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
    cep = StringField('CEP', validators=[Length(max=10)])
    telefone1 = StringField('Telefone1', validators=[Length(max=20)])
    telefone2 = StringField('Telefone2', validators=[Length(max=20)])
    email = StringField('Email', validators=[DataRequired(), Length(max=50)])
    ativo = BooleanField('Ativo')
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
    codigointerno = StringField('Cód.Int', validators=[Length(max=20)])
    ean = StringField('EAN', validators=[Length(max=13)])
    dun = StringField('DUN', validators=[Length(max=14)])

    cor = StringField('Cor', validators=[Length(min=2, max=20)])
    tamanho = StringField('Tamanho', validators=[Length(max=10)])
    largura = DecimalField('Largura')
    altura = DecimalField('Altura')
    comprimento = DecimalField('Compr.')

    pesoliquido = DecimalField('Peso Liq.')
    pesobruto = DecimalField('Peso Br.')
    estoqueminino = IntegerField('Est.Min.')
    estoquemaximo = IntegerField('Est.Max.')
    leadtime = IntegerField('LeadTime')

    loteminino = IntegerField('Lote Min.')
    lotemaximo = IntegerField('Lote Max.')
    ncm = StringField('NCM', validators=[Length(min=4, max=20)])
    cest = StringField('CEST', validators=[Length(min=4, max=20)])
    classificacao = SelectField('Classificação', 
        choices=[   ("", "ESCOLHA UMA CLASSIFICAÇÃO"),
                    (1, "[1] - Produto para Revenda"),
                    (2, "[2] - Produção Própria"),
                    (3, "[3] - Serviço Prestado"),
                    (4, "[4] - Uso e Consumo"),
                    (5, "[5] - Serviços Diversos"),
                    (9, "[9] - Ativo Imobilizado")])
    
    ativo = BooleanField('Ativo')
    id = StringField('ID')
    id_company = SelectField('Company')


class ModelFormGroup(FlaskForm):
    description = StringField('Descrição', validators=[DataRequired(), Length(min=4, max=20)])
    id = StringField('ID')


class ModelFormProduct(FlaskForm):
    name = StringField('Nome', validators=[DataRequired(), Length(min=4, max=50)])
    description = StringField('Descrição', validators=[DataRequired(), Length(min=4, max=150)])
    price = DecimalField('Preço')
    discount = DecimalField('Desconto')
    stock = IntegerField('Estoque')
    colors = StringField('Cores', validators=[Length(min=2, max=50)])
    image = FileField('Imagem')
    id = StringField('ID')
    id_brand = SelectField('Brand')
    id_category = SelectField('Category')
    id_company = SelectField('Company')