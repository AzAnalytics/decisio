#🧭 Décisio – Le pilotage automatisé, clair et intelligent

Décisio est une solution open framework de pilotage d’entreprise développée en Python.
Elle automatise la collecte, le nettoyage et la visualisation des données financières et opérationnelles pour offrir une vision claire, fiable et prédictive de la performance.

#🚀 Pourquoi Décisio ?

Dans 80 % des entreprises, les dirigeants passent encore des heures à manipuler Excel avant chaque décision.
Les données sont éparpillées, les chiffres jamais à jour, et les décisions souvent prises… au feeling.

Décisio change la donne :

connectez vos données, laissez l’automatisation travailler, et concentrez-vous enfin sur vos décisions.

#🧠 En une phrase :

De la donnée brute à la décision éclairée — sans usine à gaz, sans dépendance technique.

#⚙️ Fonctionnalités principales

✅ Ingestion automatique des données
Connectez vos fichiers Excel, CSV, API ou bases externes : Décisio les lit et les structure automatiquement.

✅ Nettoyage et validation intelligente
Les scripts intégrés détectent incohérences, doublons, erreurs de typage et assurent une donnée propre.

✅ Base de données centralisée
Toutes les données sont stockées dans PostgreSQL (ou SQLite en local) avec un schéma multi-entreprises.

✅ API FastAPI intégrée
Exposez vos métriques et indicateurs via une API rapide, documentée et sécurisée.

✅ Interface de pilotage Streamlit
Des tableaux de bord interactifs pour visualiser vos ventes, marges, dépenses ou prévisions en temps réel.

✅ Prévisions et alertes automatiques
Basé sur Prophet / scikit-learn : projections de trésorerie, tendances, détection d’anomalies.

✅ Export & reporting automatique
Générez vos rapports PDF et Excel à la volée — manuellement ou via planification quotidienne.

✅ Architecture modulaire
Chaque brique (ETL, API, dashboard) est indépendante et réutilisable. Plug-and-play.

🏗️ Architecture technique
```Client Data Sources
│
├── (1) Ingestion        →  Excel / CSV / API connectors
├── (2) Transformation   →  pandas + SQLAlchemy + rules.yaml
├── (3) Stockage         →  PostgreSQL / SQLite
├── (4) API backend      →  FastAPI
├── (5) UI dashboards    →  Streamlit + Plotly
├── (6) Forecast & IA    →  Prophet / sklearn
└── (7) Reporting        →  PDF / Excel exports
```
📂 Structure du projet
```
decisio/
│
├── app/                → Interface Streamlit (UI)
├── api/                → Backend FastAPI
├── data_pipeline/      → Extraction, transformation, chargement
├── forecasting/        → Modules de prévisions et détection d’anomalies
├── reporting/          → Génération PDF / Excel automatisée
├── clients/            → Configurations par entreprise cliente
├── core/               → Paramètres, logs, exceptions
├── tests/              → Tests unitaires et intégration
├── docker-compose.yml  → Stack complète (API + DB + UI)
└── README.md
```

#🧱 Philosophie Décisio

Simple à déployer, puissant à faire évoluer.

L’objectif n’est pas de créer un SaaS fermé, mais un framework data adaptable :
chaque consultant, freelance ou DAF peut le cloner, l’adapter à son métier, et bâtir sa propre solution de pilotage.

Décisio est pensé pour être :

💡 Lisible : code clair, doc à jour

⚙️ Modulaire : chaque brique peut vivre seule

🧩 Reproductible : même structure, plusieurs clients

🔒 Sûr : environnements isolés, configuration claire
