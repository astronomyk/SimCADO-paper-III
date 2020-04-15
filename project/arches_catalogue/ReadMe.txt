J/A+A/631/A20   GALACTICNUCLEUS JHKs imaging survey. II.  (Nogueras-Lara+, 2019)
================================================================================
GALACTICNUCLEUS: A high angular resolution JHKs imaging survey of the Galactic
Centre.
II. First data release of the catalogue and the most detailed CMDs of the GC.
    Nogueras-Lara F., Schoedel R., Gallego-Calvente A.T., Dong H.,
    Gallego-Cano E., Shahzamanian B., Girard J.H.V., Nishiyama S., Najarro F.,
    Neumayer N.
    <Astron. Astrophys. 631, A20 (2019)>
    =2019A&A...631A..20N        (SIMBAD/NED BibCode)
================================================================================
ADC_Keywords: Milky Way ; Galactic center ; Photometry, infrared ; Extinction
Keywords: Galaxy: centre - Galaxy, bulge - Galaxy: structure -
          stars: horizontal-branch - dust, extinction

Abstract:
    The high extinction and extreme source crowding of the central regions
    of the Milky Way are serious obstacles to the study of the structure
    and stellar population of the Galactic centre (GC). Surveys that cover
    the GC region (2MASS, UKIDSS, VVV, SIRIUS) do not have the necessary
    high angular resolution. Therefore, a high angular resolution survey
    in the near infrared is crucial to improve the state of the art. Here,
    we present the GALACTICNUCLEUS catalogue, a near infrared JHKs high
    angular resolution (0.2") survey of the nuclear bulge of the
    Milky Way. We explain in detail the data reduction, data analysis,
    calibration, and uncertainty estimation of the GALACTICNUCLEUS survey.
    We assess the data quality comparing our results with previous
    surveys. We obtained accurate JHKs photometry ~3.3x10^6^ stars in the
    GC detecting around 20% in J, 65% in H and 90% in Ks. The survey
    covers a total area of ~0.3 square degrees, which corresponds to
    ~6000pc^2^. The GALACTICNUCLEUS survey reaches 5 sigma detections for
    J~22mag, H~21mag and Ks~21mag. The uncertainties are below 0.05mag at
    J~21mag, H~19mag and Ks~18mag. The zero point systematic uncertainty
    is <~0.04mag in all three bands. We present colour-magnitude diagrams
    for the different regions covered by the survey.

Description:
    Catalogues specified in Table 1 of the manuscript. This is 7
    catalogues for the different regions covered by the GALACTICNUCLEUS
    catalogue: Central, NSD East, NSD West, Transition East, Transition
    West, Inner Bulge North and Inner Bulge South. The catalogues follow
    the structure presented in Table 2.

File Summary:
--------------------------------------------------------------------------------
 FileName   Lrecl  Records  Explanations
--------------------------------------------------------------------------------
ReadMe         80        .  This file
central.dat   239  2009522  GALACTICNUCLEUS. Pointings 1-30 (Central)
                             (corrected version, 31-03-2020)
nsdeast.dat   239   488197  GALACTICNUCLEUS. Pointings D12-D18 (NSD East)
                             (corrected version, 31-03-2020)
nsdwest.dat   239   199481  GALACTICNUCLEUS. Pointings D9-D11, D19, D21
                             (NSD West) (corrected version, 31-03-2020)
teast.dat     239   162830  GALACTICNUCLEUS. Pointings T3-T4
                             (Transition East) (corrected version, 31-03-2020)
twest.dat     239   167985  GALACTICNUCLEUS. Pointings T7-T8
                             (Transition West) (corrected version, 31-03-2020)
ibnorth.dat   239    90300  GALACTICNUCLEUS. Pointings B1, B6
                             (Inner Bulge North) (corrected version, 31-03-2020)
ibsouth.dat   239   159607  GALACTICNUCLEUS. Pointings B2, B5
                             (Inner Bulge South) (corrected version, 31-03-2020)
--------------------------------------------------------------------------------

See also:
   J/A+A/610/A83 : GALACTICNUCLEUS: JHKs imaging survey (Nogueras-Lara+, 2018)

Byte-by-byte Description of file: *.dat
--------------------------------------------------------------------------------
   Bytes Format Units     Label     Explanations
--------------------------------------------------------------------------------
   1-  9  F9.5  deg       RAdeg     Right ascension combining detections (J2000)
                                     (ra)
  11- 21  F11.9 arcsec  e_RAdeg     Uncertainty on RA (dra)
  23- 32  F10.6 deg       DEdeg     Declination combining detections (J2000)
                                     (dec)
  34- 44  F11.9 arcsec  e_DEdeg     Uncertainty on DE (ddec)
  46- 54  F9.5  deg       RAJdeg    ?=0 Right ascension J-band detection (J2000)
                                     (raJ) (1)
  56- 66  F11.9 arcsec  e_RAJdeg    ?=0 Uncertainty on RAJ (draJ)
  68- 77  F10.6 deg       DEJdeg    ?=0 Declination J-band detection (J2000)
                                     (decJ) (1)
  79- 89  F11.9 arcsec  e_DEJdeg    ?=0 Uncertainty on DEJ (ddecJ)
  91- 99  F9.5  deg       RAHdeg    ?=0 Right ascension H-band detection (J2000)
                                     (raH) (1)
 101-111  F11.9 arcsec  e_RAHdeg    ?=0 Uncertainty on RAH (draH)
 113-122  F10.6 deg       DEHdeg    ?=0 Declination H-band detection (J2000)
                                    (decH) (1)
 124-134  F11.9 arcsec  e_DEHdeg    ?=0 Uncertainty on DEH (ddecH)
 136-144  F9.5  deg       RAKsdeg   ?=0 Right ascension Ks-band detection
                                    (J2000) (raKs) (1)
 146-156  F11.9 arcsec  e_RAKsdeg   ?=0 Uncertainty on RAKs (draKs)
 158-167  F10.6 deg       DEKsdeg   Declination Ks-band detection (J2000)
                                     (decKs) (1)
 169-179  F11.9 arcsec  e_DEKsdeg   ?=0 Uncertainty on DEKs (ddecKs)
 181-188  F8.5  mag       Jmag      ?=99 J-band magnitude (J) (2)
 190-197  F8.5  mag     e_Jmag      ?=99 Uncertainty on J-band magnitude (dJ)
 199-206  F8.5  mag       Hmag      ?=99 H-band magnitude (H) (2)
 208-215  F8.5  mag     e_Hmag      ?=99 Uncertainty on H-band magnitude (dH)
 217-224  F8.5  mag       Ksmag     ?=99 Ks-band magnitude (Ks) (2)
 226-233  F8.5  mag     e_Ksmag     ?=99 Uncertainty on Ks-band magnitude (dKs)
     235  I1    ---       iJ        J-band detection in iJ pointings (iJ) (3)
     237  I1    ---       iH        H-band detection in iH pointings (iH) (3)
     239  I1    ---       iKs       Ks-band detection in iKs pointings (iKs) (3)
--------------------------------------------------------------------------------
Note (1): A coordinate value equals to zero means that a star was not detected
  in a given band.
Note (2): A magnitude value equals to 99 indicates that there is no detection
  for a given source.
Note (3): iJ, iH and iKs indicate the number of fields where a star were
  detected to obtain its final photometry.
--------------------------------------------------------------------------------

History:
    From Francisco Nogueras-Lara, fnoguer(ay)iaa.es

Acknowledgements:
    The research leading to these results has received funding from the
    European Research Council under the European Union's Seventh Framework
    Programme (FP7/2007-2013) / ERC grant agreement No [614922]. This
    work is based on observations made with ESO Telescopes at the La Silla
    Paranal Observatory under programmes IDs 195.B-0283 and 091.B-0418. We
    thank the staff of ESO for their great efforts and helpfulness. Author
    F N-L acknowledges financial support from the State Agency for
    Research of the Spanish MCIU through the "Center of Excellence Severo
    Ochoa" award for the Instituto de Astrofisica de Andalucia
    (SEV-2017-0709). F N-L acknowledges financial support from a MECD
    pre-doctoral contract, code FPU14/01700. F N acknowledges financial
    support through Spanish grants ESP2015-65597-C4-1-R and
    ESP2017-86582-C4-1-R (MINECO/FEDER). N.N. acknowledges support by
    Sonderforschungsbereich SFB 881 'The Milky Way System' (subproject B8)
    of the German Research Foundation (DFG).

References:
    Nogueras-Lara F.,  Paper I   2018A&A...610A..83N, Cat. J/A+A/610/A83

History:
    15-Oct-2019: on-line version
    31-Mar-2020: corrected files, from author

================================================================================
(End) F. Nogueras-Lara [IAA-CSIC, Spain], P. Vannier [CDS]           21-Aug-2019
