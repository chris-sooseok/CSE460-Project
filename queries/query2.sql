DELETE FROM property
WHERE number = 99
  AND street = 'MAIN ST'
  AND city = 'Cheektowaga'
  AND zip_code = '14001';

DELETE FROM address
WHERE number = 99
  AND street = 'MAIN ST'
  AND city = 'Cheektowaga'
  AND zip_code = '14001';