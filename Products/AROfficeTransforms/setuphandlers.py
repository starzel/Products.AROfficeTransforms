from Products.MimetypesRegistry import MimeTypeItem
from Products.CMFCore.utils import getToolByName

from Products.AROfficeTransforms.config import TRANSFORMS


def install(self):
    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.
    if self.readDataFile('Products.AROfficeTransforms-tranforms.txt') is None:
        return
    #
    transform_tool = getToolByName(self, 'portal_transforms')
    for transform in TRANSFORMS:
        print "atReal : Adding %s transform" % transform
        # Remove existing transform, if any
        if transform in transform_tool.objectIds():
            transform_tool.manage_delObjects([transform])
        transform_tool.manage_addTransform(transform, 'Products.AROfficeTransforms.transforms.'+transform)
        print "atReal : %s added" % transform


def uninstall(self):
    transform_tool = getToolByName(self, 'portal_transforms')
    for transform in TRANSFORMS:
        print "atReal : Deleting %s transform" % transform
        if transform in transform_tool.objectIds():
            try:
                transform_tool.manage_delObjects([transform])
            except Exception, e:
                print e.__class__.__name__, str(e)
