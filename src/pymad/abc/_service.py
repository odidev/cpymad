'''
Created on 15 Aug 2011

@author: kfuchsbe
'''
from io import __metaclass__
from abc import ABCMeta, abstractmethod, abstractproperty

class PyMadService():
    ''' The abstract class for a model-service. '''
    __metaclass__ = ABCMeta
    
    @abstractproperty
    def mdefs(self):
        ''' Returns all the available model definitions as a list '''
        pass
    
    @abstractproperty
    def models(self):
        ''' Returns all the instantiated models as a list '''
        pass
    
    @abstractmethod
    def create_model(self, modeldef):
        """Create a model instance from a model definition.

        Arguments:
        modeldef -- the model definition from which to create the model.
        
        """
        pass
    
