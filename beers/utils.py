
def image_upload_location(instance, filename):
    return 'media/beer/images/%s.png' % (instance.id)