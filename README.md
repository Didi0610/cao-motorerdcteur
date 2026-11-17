# Motoréducteur Bonfiglioli VF/W 30/63_1200 — P56 — BN56A4 (CAO 3D)

Reconstruction CAO 3D (STEP) du motoréducteur combiné roue-et-vis désigné dans le
catalogue Bonfiglioli série VF/W : **VF/W 30/63_1200, P56, BN56A4**
(0,06 kW — 1,1 tr/min — M2 = 122 Nm — i = 1200 — Rn2 = 5000 N).

## Contenu

| Fichier | Description |
|---|---|
| `VF_W_30_63_1200_P56_BN56A4.step` | Modèle STEP AP214 (mm), 2 solides : `gearbox_body` + `motor_BN56A4` |
| `build_vfw3063.py` | Script de génération (Python + CadQuery) |

## Cotes d'interface (catalogue Bonfiglioli VF/W, R11)

- **Sortie (version U)** : alésage Ø25 H7 traversant, clavette 8 H8 (entraxe 28,3), moyeu Ø75 h8 en dépassement
- **Bride d'entrée P56 B5** : Ø120, cercle de perçage Ø100 (4×Ø7), épaulement Ø80, épaisseur 9, alésage Ø9 E7 + clavette 3 H9 (entraxe 10,4)
- **Moteur BN 56A4 (IM B5)** : carter Ø110 (AC), bride P=120 / M=100 / N=80 / S=7 / T=3, arbre 9×20 clavetté, boîte à bornes (AD=91, AF=74), capot de ventilation
- **Cinématique** : deux étages roue-et-vis en série → axe moteur parallèle à l'axe de sortie ; entraxes 30 (VF30) et 63 (W63) ; chaîne axiale réducteur 9 + 76 + 94 + 3,5 = 182,5 mm
- **Encombrement** : 400,5 × 120 × 227,5 mm

## Réserve

Les cotes d'interface (alésages, brides, moyeu, fixations) sont fidèles au catalogue.
L'enveloppe des carters est une reconstruction représentative : le catalogue ne
fournit pas toutes les cotes de carrosserie.

## Régénérer

```bash
pip install cadquery
python build_vfw3063.py
```
