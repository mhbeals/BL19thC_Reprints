### Reprints within the British Library's 19th Century Newspapers Collection

#### Raw Matching Reports

The Raw Matching Reports directory contain manifests of reprints from the British Library's 19th Century Newspapers Collection. Each manifest contains a list of matches from a single year. The year relates the *source* or *earlier* text; the *target* or *later* text will be within 18 months. Manual testing suggested that matches more than 18 months apart were almost consistently always false positives, with some miscellany or advertising material. As the aim of this project is to identify reprinted news or time-sensitive material matches over 18 months have not been included. If you wish to replicate the matching procedure, or obtain matches over 18 months, the steps required to re-run the matching exercises are included below.

Each line represents two pages from the collection that contain a substantial amount of similar text. They were identified using Lou Bloomfield's [Copyfind](http://plagiarism.bloomfieldmedia.com/wordpress/software/copyfind/) plagiarism detection software using the following procedure:

1. Transform original page-level XML data from British Library into plaintext files using BL_TEXT.xsl
2. Run plaintext files through Copyfind in overlapping five-year sets using custom script files
3. Transform manifest files created by Copyfind to clean Tab-Separated Value (.tsv) files by   
  a. Removing file paths   
  b. Removing file extensions (.txt)   
  c. Replacing full stops (.) and underscores (_) with tab characters  

#### Directed Links

The Directed Links directory contains manifests of direct reprinting relationships within the British Library's 19th Century Newspapers Collection. Each manifest contains a list of matches from a single year. The year relates the *source* or *earlier* text; the *target* or *later* text will be within 200 days. Manual testing suggested that matches more than 200 days apart were almost consistently always false positives, miscellany or advertising material. As the aim of this project is to identify reprinted news or time-sensitive material matches over 200 days have not been included. Testing also suggests that, with rare excepting, matches within the same periodical was consistently a false positive or advertising material. Therefore, matches from within the same periodical have not been included. Finally, as the titles tested do not consistently represent morning or evening editions, matches which have the same date of publication have not been included. Other "impossible" date combinations (such as reprinting in London and Aberdeen one day apart) have **not** been excluded at this stage.

Each line represents two pages from the collection that likely have a direct ancestor-descendent relationship. Although intermediary like occur, both likely exist on the same branch of the evolutionary tree. Matches were identified using the Reprint Mapper, using the following steps.

Raw Match Reports from Copyfind (before step 3) were inputted into the Reprint Mapper, which filtered out any matches that were

1. In the same title
2. Published on the same day
3. More than 200 days apart

It then filtered out any match in which neither

1. The Perfect Match was at least 160 Characters
2. The Left match was at least 90 Characters
3. The Right Match was at least 90 Characters

This reduced the likelihood of false positives based on small matches, but was more precise than the original Copyfind options allowed. Then, for each *target*, the Mapper found the *source* with the highest Perfect Match. If more than one source had the same Perfect Match score, the earliest source was chosen. The Mapper then printed a manifest, linking a source to each target; it did not necessarily match a target to each source; sources without targets represent evolutionary dead ends.
