# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 16:59:44 2016

@author: Standard
"""
def xml2B2d(filePath):
    from lxml import etree
    import io
# Les variables sont chargés via le formulaire html
# Le chargement
    doc = etree.parse(io.BytesIO(filePath))
    root = doc.getroot()
#Analyser le fichier xml pour remplacer les attributs voulus
    tree = etree.ElementTree(root)
    for e in root.iter():
        if tree.getpath(e) == "/gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString":
            POC_Organisation_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:dateStamp/gco:DateTime":
            Creation_date_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString":
            Title_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:abstract/gco:CharacterString":
            Abstract_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty[1]/gmd:organisationName/gco:CharacterString" or tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString":
            OW1_Organisation_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]":
            OW1_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty[2]/gmd:organisationName/gco:CharacterString":
            OW2_Organisation_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString":
            D_Organisation_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[1]/gmd:MD_Keywords":
            subject_study0_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[2]/gmd:MD_Keywords":
            project_phase0_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[3]/gmd:MD_Keywords":
            location0_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[4]/gmd:MD_Keywords":
            variable0_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:useLimitation/gco:CharacterString":
            Use_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[1]/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod/gml:beginPosition":
            Date1_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[1]/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod/gml:endPosition":
            Date2_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[2]/gmd:EX_Extent/gmd:verticalElement/gmd:EX_VerticalExtent/gmd:minimumValue/gco:Real":
            Depth1_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[2]/gmd:EX_Extent/gmd:verticalElement/gmd:EX_VerticalExtent/gmd:maximumValue/gco:Real":
            Depth2_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[3]/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/gco:Decimal":
            West_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[3]/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/gco:Decimal":
            East_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[3]/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/gco:Decimal":
            South_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[3]/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/gco:Decimal":
            North_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution/gmd:distributionFormat/gmd:MD_Format":
            format0_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:dataQualityInfo[1]/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:statement/gco:CharacterString":
            Quality_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:dataQualityInfo[1]/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:processStep/gmd:LI_ProcessStep/gmd:description/gco:CharacterString":
            Process_step_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:dataQualityInfo[1]/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:processStep/gmd:LI_ProcessStep/gmd:source/gmd:LI_Source/gmd:description/gco:CharacterString":
            Citation_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:dataQualityInfo[1]/gmd:DQ_DataQuality/gmd:scope/gmd:DQ_Scope/gmd:level/gmd:MD_ScopeCode":
            Data_type_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:accessConstraints/gmd:MD_RestrictionCode":
            access_xml = e
#Remplisage du fichier xml pour chaque donnée

    title = Title_xml.text
    abstract = Abstract_xml.text
    data_type = Data_type_xml.attrib['codeListValue']
    North = float(North_xml.text)
    East = float(East_xml.text)
    South = float(South_xml.text)
    West = float(West_xml.text)
    Depth1 = float(Depth1_xml.text)
    Depth2 = float(Depth2_xml.text)
    Creation_date = Creation_date_xml.text
    T1 = Date1_xml.text
    (t1, h1) = T1.split('T')
    T2 = Date2_xml.text
    if isinstance(T2, str):
        [t2, h2] = T2.split('T')
        T3 = 1
    else:
        T3 = 0
        t2 = None
        h2 = None

    subject_Study = []
    Len_su = len(subject_study0_xml)
    for i in range(0, Len_su - 2):
        subject_Study.append(subject_study0_xml[i][0].text)

    project_Phase = []
    Len_pro = len(project_phase0_xml)
    for i in range(0, Len_pro - 2):
        project_Phase.append(project_phase0_xml[i][0].text)

    location = []
    Len_loc = len(location0_xml)
    for i in range(0, Len_loc-2):
        location.append(location0_xml[i][0].text)


    variables = []
    Len_var = len(variable0_xml)
    for i in range(0, Len_var-2):
        variables.append(variable0_xml[i][0].text)

    format1 = []
    Len_for = len(format0_xml)
    for i in range(0, Len_for - 1):
        format1.append(format0_xml[i][0].text)

    quality = Quality_xml.text
    process = Process_step_xml.text
    use_lim = Use_xml.text
    access = access_xml.attrib['codeListValue']
    citation = Citation_xml.text

    if len(OW1_xml) == 0:
        owner1 = 0
        owner2 = 0
    elif len(OW1_xml) == 1:
        owner1 = OW1_Organisation_xml.text
        owner2 = 0
    elif len(OW1_xml) == 2:
        owner1 = OW1_Organisation_xml.text
        owner2 = OW2_Organisation_xml.text

    resource_contact = POC_Organisation_xml.text
    distributor = D_Organisation_xml.text
    print(title, abstract, data_type, North, East, South, West, Depth1, Depth2,
          T1, T2, T3, t1, h1, t2, h2, Creation_date, subject_Study, project_Phase,
          location, variables, format1, quality, process, use_lim, access, citation,
          resource_contact, owner1, owner2, distributor)
    return title, abstract,data_type, North, East, South, West, Depth1, Depth2, T1, T2, T3, t1, h1, t2, h2, Creation_date, subject_Study, project_Phase, location, variables, format1, quality, process, use_lim, access, citation, resource_contact, owner1, owner2, distributor
