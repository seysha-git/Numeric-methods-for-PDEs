# Svar på oppgavene

## 1. Gjenta eksperimentet med ℎ = 0.01, ℎ = 0.001 osv, og se hva som skjer. Hvor liten ℎ kan du ta før det går åt skogen?
**Svar:**  
Det tok 9 iterasjoner før feilen begynte å vokse (se oppgave1.py).

## 2. Hvor liten ℎ kan du nå (sekantmetoden) ta før det går åt skogen? Bruk Taylorrekker til å forklare oppførselen.
**Svar:**  
Det tok 6 iterasjoner før feilen begynte å vokse (oppgave2.py). Fikk mer presis approksimasjon ettersom feilen er proporsjonal med ℎ. Går raskere åt skogen da feilen inneholder høyere ordens Taylor-ledd (for små ℎ blir avrundingsfeil dominerende).

## 3. Eksplisitt metode, Implisitt metode og Crank-Nicolson metode:
- Med eksplisitt metode er det tydelig med animasjon at k/h^2 = r <= 1/2  for å unngå numerisk ustabilitet.
- For implisitt metode og Crank-Nicolson løste jeg likningssystemene som foreslått i kompendiumet. 
- Den implisitte metoden var mer stabil, men for k og h liten nok, gadd ikke programmet å kjøre.
- Crank-Nicolson var også stabil, og litt raskere.
- **Kort sammenligning:**  
    - Eksplisitt: Enklere å implementere, men ikke alltid stabil.  
    - Implisitt og Crank-Nicolson: Mer beregningstunge, men stabilere.  
    - Crank-Nicolson var raskere enn implisitt.


Kilde: https://www.math.ntnu.no/emner/TMA4125/2019v/notater/11-numerikk-for-pde.pdf


