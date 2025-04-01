# Svar på oppgavene

## 1. Gjenta eksperimentet med ℎ = 0.01, ℎ = 0.001 osv, og se hva som skjer. Hvor liten ℎ kan du ta før det går åt skogen?
**Svar:**  
Det tok 9 iterasjoner før feilen begynte å vokse (se oppgave1.py).

## 2. Hvor liten ℎ kan du nå ta før det går åt skogen? Bruk Taylorrekker til å forklare oppførselen.
**Svar:**  
Det tok 6 iterasjoner før feilen begynte å vokse (oppgave2.py). Fikk mer presis approksimasjon ettersom feilen er proporsjonal med ℎ. Går raskere åt skogen siden feilen inkluderer høyere orden taylor-ledd, og liten h får de høyere ordens leddende til å bidra mer til feilen. 

## 4, 5, 6. Eksplisitt metode, Implisitt metode og Crank-Nicolson metode:
- Med eksplisitt metode er det tydelig med animasjon at k/h^2 = r <= 1/2  for å unngå numerisk ustabilitet.
- For implisitt metode og Crank-Nicolson løste jeg likningssystemene som foreslått i kompendiumet, men naturligvis treigere 
- Den implisitte metoden var mer stabil, men for k og h liten nok, gadd ikke programmet å kjøre.
- Crank-Nicolson var også stabil, og litt raskere.

Kilde: https://www.math.ntnu.no/emner/TMA4125/2019v/notater/11-numerikk-for-pde.pdf
## Bonus
-Noe spennende jeg har jobbet med på egenhånd er et lite spill i c++: https://github.com/seysha-git/GameDev


