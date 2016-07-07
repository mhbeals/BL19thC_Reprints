# Reprints of the British Library's 19th Century Newspapers Collection
*A collection of manifests describing scissors-and-paste reprints within the British Library's 19th Century Newspapers Collection*

The following directories contain manifests of reprints from the British Library's 19th Century Newspapers Collection. Each manifest contains a list of matches; each line represents two pages from the collection that contain a substantial amount of similar text. They were created using Lou Bloomfield's [Copyfind](http://plagiarism.bloomfieldmedia.com/wordpress/software/copyfind/) plagiarism detection software using the following procedure:

1. Transform original page-level XML data from British Library into plaintext files using BL_TEXT.xsl
2. Run plaintext files through Copyfind in overlapping five-year sets using custom script files
3. Transform manifest files created by Copyfind to clean Tab-Separated Value (.tsv) files by   
  a. Removing file paths   
  b. Removing file extensions (.txt)   
  c. Replacing full stops (.) and underscores (_) with tab characters  
