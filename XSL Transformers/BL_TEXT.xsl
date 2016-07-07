<?xml version="1.0" encoding="UTF-8"?>
    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
        xmlns:xs="http://www.w3.org/2001/XMLSchema"
        exclude-result-prefixes="xs"
        version="2.0">
        <xsl:output method="text" encoding="UTF-8" indent="yes"/>
        <xsl:template match="/">
            <xsl:variable name="number"><xsl:number/></xsl:variable>
            <xsl:for-each select="collection(concat('file:///I:/BL_XMLS/XMLS_CHECK/1830', '?select=*.xml;recurse=no'))">
                            <xsl:for-each select="BL_newspaper">
                                <xsl:result-document method="text" href="file:///I:/BL_TXTS/Check/{substring(BL_page/issue_metadata/normalisedDate,1,4)}/{BL_page/issue_metadata/normalisedDate}_{replace(BL_page/title_metadata/title,' ','')}_S{BL_page/pageImage/pageSequence}.txt">
<xsl:for-each select="BL_page">
    <xsl:for-each select="pageText/pageWord"><xsl:value-of select="concat(.,' ')"/></xsl:for-each></xsl:for-each>
</xsl:result-document>
                </xsl:for-each></xsl:for-each>
        </xsl:template>
    </xsl:stylesheet>