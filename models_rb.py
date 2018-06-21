from peewee import *

database = SqliteDatabase('rbogus-dev.db', **{})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Images(BaseModel):
    crossmatched = BooleanField()
    path = CharField()

    class Meta:
        db_table = 'Images'

class Detected(BaseModel):
    a_image = UnknownField(db_column='A_IMAGE')  # FLOAT
    background = UnknownField(db_column='BACKGROUND')  # FLOAT
    b_image = UnknownField(db_column='B_IMAGE')  # FLOAT
    class_star = UnknownField(db_column='CLASS_STAR')  # FLOAT
    cxx_image = UnknownField(db_column='CXX_IMAGE')  # FLOAT
    cxy_image = UnknownField(db_column='CXY_IMAGE')  # FLOAT
    cyy_image = UnknownField(db_column='CYY_IMAGE')  # FLOAT
    deltax = UnknownField(db_column='DELTAX')  # FLOAT
    deltay = UnknownField(db_column='DELTAY')  # FLOAT
    ellipticity = UnknownField(db_column='ELLIPTICITY')  # FLOAT
    elongation = UnknownField(db_column='ELONGATION')  # FLOAT
    flags = UnknownField(db_column='FLAGS')  # FLOAT
    fluxerr_aper = UnknownField(db_column='FLUXERR_APER')  # FLOAT
    fluxerr_auto = UnknownField(db_column='FLUXERR_AUTO')  # FLOAT
    fluxerr_iso = UnknownField(db_column='FLUXERR_ISO')  # FLOAT
    flux_aper = UnknownField(db_column='FLUX_APER')  # FLOAT
    flux_auto = UnknownField(db_column='FLUX_AUTO')  # FLOAT
    flux_iso = UnknownField(db_column='FLUX_ISO')  # FLOAT
    flux_max = UnknownField(db_column='FLUX_MAX')  # FLOAT
    fwhm_image = UnknownField(db_column='FWHM_IMAGE')  # FLOAT
    is_real = BooleanField(db_column='IS_REAL', null=True)
    magerr_aper = UnknownField(db_column='MAGERR_APER')  # FLOAT
    magerr_auto = UnknownField(db_column='MAGERR_AUTO')  # FLOAT
    magerr_iso = UnknownField(db_column='MAGERR_ISO')  # FLOAT
    mag_aper = UnknownField(db_column='MAG_APER')  # FLOAT
    mag_auto = UnknownField(db_column='MAG_AUTO')  # FLOAT
    mag_iso = UnknownField(db_column='MAG_ISO')  # FLOAT
    mu_max = UnknownField(db_column='MU_MAX')  # FLOAT
    number = IntegerField(db_column='NUMBER')
    peak_centroid = UnknownField(db_column='PEAK_CENTROID')  # FLOAT
    ratio = UnknownField(db_column='RATIO')  # FLOAT
    roundness = UnknownField(db_column='ROUNDNESS')  # FLOAT
    theta_image = UnknownField(db_column='THETA_IMAGE')  # FLOAT
    threshold = UnknownField(db_column='THRESHOLD')  # FLOAT
    x2_image = UnknownField(db_column='X2_IMAGE')  # FLOAT
    xmax_image = UnknownField(db_column='XMAX_IMAGE')  # FLOAT
    xmin_image = UnknownField(db_column='XMIN_IMAGE')  # FLOAT
    xpeak_image = UnknownField(db_column='XPEAK_IMAGE')  # FLOAT
    xy_image = UnknownField(db_column='XY_IMAGE')  # FLOAT
    x_image = UnknownField(db_column='X_IMAGE')  # FLOAT
    y2_image = UnknownField(db_column='Y2_IMAGE')  # FLOAT
    ymax_image = UnknownField(db_column='YMAX_IMAGE')  # FLOAT
    ymin_image = UnknownField(db_column='YMIN_IMAGE')  # FLOAT
    ypeak_image = UnknownField(db_column='YPEAK_IMAGE')  # FLOAT
    y_image = UnknownField(db_column='Y_IMAGE')  # FLOAT
    image = ForeignKeyField(db_column='image_id', null=True, rel_model=Images, to_field='id')

    class Meta:
        db_table = 'Detected'

class Bogus(BaseModel):
    detected = ForeignKeyField(db_column='detected_id', null=True, rel_model=Detected, to_field='id')

    class Meta:
        db_table = 'Bogus'

class Imagesois(BaseModel):
    crossmatched = BooleanField()
    path = CharField()

    class Meta:
        db_table = 'ImagesOIS'

class Detectedois(BaseModel):
    a_image = UnknownField(db_column='A_IMAGE')  # FLOAT
    background = UnknownField(db_column='BACKGROUND')  # FLOAT
    b_image = UnknownField(db_column='B_IMAGE')  # FLOAT
    class_star = UnknownField(db_column='CLASS_STAR')  # FLOAT
    cxx_image = UnknownField(db_column='CXX_IMAGE')  # FLOAT
    cxy_image = UnknownField(db_column='CXY_IMAGE')  # FLOAT
    cyy_image = UnknownField(db_column='CYY_IMAGE')  # FLOAT
    deltax = UnknownField(db_column='DELTAX')  # FLOAT
    deltay = UnknownField(db_column='DELTAY')  # FLOAT
    ellipticity = UnknownField(db_column='ELLIPTICITY')  # FLOAT
    elongation = UnknownField(db_column='ELONGATION')  # FLOAT
    flags = UnknownField(db_column='FLAGS')  # FLOAT
    fluxerr_aper = UnknownField(db_column='FLUXERR_APER')  # FLOAT
    fluxerr_auto = UnknownField(db_column='FLUXERR_AUTO')  # FLOAT
    fluxerr_iso = UnknownField(db_column='FLUXERR_ISO')  # FLOAT
    flux_aper = UnknownField(db_column='FLUX_APER')  # FLOAT
    flux_auto = UnknownField(db_column='FLUX_AUTO')  # FLOAT
    flux_iso = UnknownField(db_column='FLUX_ISO')  # FLOAT
    flux_max = UnknownField(db_column='FLUX_MAX')  # FLOAT
    fwhm_image = UnknownField(db_column='FWHM_IMAGE')  # FLOAT
    is_real = BooleanField(db_column='IS_REAL', null=True)
    magerr_aper = UnknownField(db_column='MAGERR_APER')  # FLOAT
    magerr_auto = UnknownField(db_column='MAGERR_AUTO')  # FLOAT
    magerr_iso = UnknownField(db_column='MAGERR_ISO')  # FLOAT
    mag_aper = UnknownField(db_column='MAG_APER')  # FLOAT
    mag_auto = UnknownField(db_column='MAG_AUTO')  # FLOAT
    mag_iso = UnknownField(db_column='MAG_ISO')  # FLOAT
    mu_max = UnknownField(db_column='MU_MAX')  # FLOAT
    number = IntegerField(db_column='NUMBER')
    peak_centroid = UnknownField(db_column='PEAK_CENTROID')  # FLOAT
    ratio = UnknownField(db_column='RATIO')  # FLOAT
    roundness = UnknownField(db_column='ROUNDNESS')  # FLOAT
    theta_image = UnknownField(db_column='THETA_IMAGE')  # FLOAT
    threshold = UnknownField(db_column='THRESHOLD')  # FLOAT
    x2_image = UnknownField(db_column='X2_IMAGE')  # FLOAT
    xmax_image = UnknownField(db_column='XMAX_IMAGE')  # FLOAT
    xmin_image = UnknownField(db_column='XMIN_IMAGE')  # FLOAT
    xpeak_image = UnknownField(db_column='XPEAK_IMAGE')  # FLOAT
    xy_image = UnknownField(db_column='XY_IMAGE')  # FLOAT
    x_image = UnknownField(db_column='X_IMAGE')  # FLOAT
    y2_image = UnknownField(db_column='Y2_IMAGE')  # FLOAT
    ymax_image = UnknownField(db_column='YMAX_IMAGE')  # FLOAT
    ymin_image = UnknownField(db_column='YMIN_IMAGE')  # FLOAT
    ypeak_image = UnknownField(db_column='YPEAK_IMAGE')  # FLOAT
    y_image = UnknownField(db_column='Y_IMAGE')  # FLOAT
    image = ForeignKeyField(db_column='image_id', null=True, rel_model=Imagesois, to_field='id')

    class Meta:
        db_table = 'DetectedOIS'

class Bogusois(BaseModel):
    detected = ForeignKeyField(db_column='detected_id', null=True, rel_model=Detectedois, to_field='id')

    class Meta:
        db_table = 'BogusOIS'

class Simulated(BaseModel):
    app_mag = UnknownField()  # FLOAT
    code = IntegerField(null=True)
    image = ForeignKeyField(db_column='image_id', null=True, rel_model=Images, to_field='id')
    image_id_ois = ForeignKeyField(db_column='image_id_ois', null=True, rel_model=Imagesois, to_field='id')
    x = UnknownField()  # FLOAT
    y = UnknownField()  # FLOAT

    class Meta:
        db_table = 'Simulated'

class Reals(BaseModel):
    detected = ForeignKeyField(db_column='detected_id', null=True, rel_model=Detected, to_field='id')
    simulated = ForeignKeyField(db_column='simulated_id', null=True, rel_model=Simulated, to_field='id')

    class Meta:
        db_table = 'Reals'

class Realsois(BaseModel):
    detected = ForeignKeyField(db_column='detected_id', null=True, rel_model=Detectedois, to_field='id')
    simulated = ForeignKeyField(db_column='simulated_id', null=True, rel_model=Simulated, to_field='id')

    class Meta:
        db_table = 'RealsOIS'

class Undetected(BaseModel):
    simulated = ForeignKeyField(db_column='simulated_id', null=True, rel_model=Simulated, to_field='id')

    class Meta:
        db_table = 'Undetected'

class Undetectedois(BaseModel):
    simulated = ForeignKeyField(db_column='simulated_id', null=True, rel_model=Simulated, to_field='id')

    class Meta:
        db_table = 'UndetectedOIS'

class CorralAlerted(BaseModel):
    alert_path = CharField(null=True)
    created_at = DateTimeField(null=True)
    model_ids = BlobField(null=True)
    model_table = CharField(null=True)

    class Meta:
        db_table = '__corral_alerted__'

