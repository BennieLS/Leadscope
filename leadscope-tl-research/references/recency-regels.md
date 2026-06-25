# Recency-regels (180 dagen, geverifieerd)

Het belangrijkste mechanisme van deze skill. Een naïeve aanpak vult de shortlist met oude koek omdat **zoekrelevantie niet hetzelfde is als recentheid**. Een SEO-sterk evergreen-artikel ("Wat is GTM-engineering?") rankt jarenlang bovenaan. Als je op zoekpositie vertrouwt, kies je oud materiaal. De recentheid komt dus niet van het zoeken, maar van deze verificatie.

## De drempeldatum

Bereken bij elke run: **vandaag minus 180 dagen**. Alles met een publicatiedatum vóór die drempel valt af. Reken dit live uit — gebruik nooit een vast jaartal of een datum uit een vorige run.

## De regels

1. **Datum verplicht, en geverifieerd aan de bron.** Lees de publicatiedatum van de pagina zelf via web_fetch (metadata zoals `published_time` / `article:published_time` / `datePublished`), niet uit het zoeksnippet. Snippets liegen over leeftijd.

2. **Geen datum = niet meenemen.** Tenzij het een onmiskenbaar tijdgebonden gebeurtenis is (een event van vorige maand, een releasedatum die elders bevestigd is).

3. **Let op "vers gepoetst, oud van binnen".** Als `modified` recent is maar `published` ver vóór de drempel ligt, is het meestal een SEO-republicatie van oude content — geen nieuws. Niet meenemen, tenzij de update zelf het nieuws is (bv. een rapport dat met verse cijfers is herzien).

4. **Brontype-voorkeur bij twijfel.** Recencygevoelige types boven evergreen: nieuws, nieuw uitgebrachte rapporten/onderzoeken, product-release-notes, podcastafleveringen en verse LinkedIn-posts > tijdloze "wat is X"-gidsen.

5. **Bij een rapport: gebruik de uitgavedatum van het rapport**, niet de datum van een artikel dat het naverteld. Zoek de oorspronkelijke release om de datum te bevestigen.

## Wat je in het zaadje noteert

Zet bij elk zaadje de **geverifieerde datum** en de **bron**. Dat maakt voor de gebruiker meteen controleerbaar dat het binnen het venster valt en waar het vandaan komt.

## Eerlijke grens

Deze skill kan recentheid niet afdwingen — het zijn instructies die jou dwingen om elke kandidaat te dateren en oude/ongedateerde items te verwerpen. Doe die verificatie echt; sla 'm niet over om sneller bij 8 zaadjes te komen. Liever 6 geverifieerde zaadjes dan 8 waarvan er 3 oud blijken.

## Voorbeeld van de val

Een zoekopdracht naar "GTM-engineering" zet een artikel bovenaan dat in februari vorig jaar is gepubliceerd en in oktober licht is bijgewerkt. Hoge positie, ziet er actueel uit — maar de publicatiedatum ligt ruim buiten 180 dagen. Verwerpen, ondanks de ranking. Dít is precies het scenario waarvoor regel 1 en 3 bestaan.
