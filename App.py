from models.ModelMail import *
from models.ModelUser import *
from models.ModelCompany import *
from models.ModelStore import *
from models.ModelProvider import *
from models.ModelClient import *
from models.ModelItem import *

from views.ViewMail import *
from views.ViewUser import *
from views.ViewCompany import *
from views.ViewStore import *
from views.ViewProvider import *
from views.ViewClient import *
from views.ViewItem import *


if __name__ == '__main__':
    app.run(debug = True)