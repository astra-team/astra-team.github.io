echo "Running hal export script"
python hal-export-to-bib.py

echo "Copying bib to ../_bibliography/rits-astra.bib"
cp rits-astra.bib ../_bibliography/rits-astra.bib

echo "All done. Just recompile jekyll website."
# echo "Converting bibtex to hugo html"
# echo "(IMPORTANT) 'Error file exists' are not real errors, should be read as 'file overwritten' (print bug in academic-cli)"
# cd .. ;
# academic import --bibtex scripts/rits-astra.bib --overwrite
