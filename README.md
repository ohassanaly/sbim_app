This repository includes the App developed for SBIM purposes. The goal is to provide an access to an internal web app, allowing to retrieve structured information from PDFs. The use-case here is drug advice documents established by HAS (Haute Autorité de Santé). Those documents are publicly available : https://www.has-sante.fr/jcms/p_3281266/fr/avis-et-decisions-sur-les-medicaments
Main architecture would include :

- PDF reader to retrieve text

- Prompt to ask for structred data extraction

- OpenAI API request to perfrom data extraction
