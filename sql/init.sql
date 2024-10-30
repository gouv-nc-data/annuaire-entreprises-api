-- Insertion des entreprises
INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT001', 'Tech Innovators', 'Tech Innov', 'SAS', '10 Rue de la Technologie', '75001', 'Paris', '10 Rue de la Technologie', '75001', 'Paris', '0145689200', 'contact@techinnovators.fr', '6201Z', 'Conseil en informatique', '6201', '6202', 25, '11-50', 'Moyenne', '2015-06-01', NULL, NULL, 'Syntec', 'RCS-75001-2020', '2020-01-15', NULL, 100000, TRUE, '31/12', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);
  
INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT002', 'Cuisine Créative', 'Cuisine Créa', 'SARL', '20 Avenue des Chefs', '69000', 'Lyon', '20 Avenue des Chefs', '69000', 'Lyon', '0472987654', 'info@cuisinecreative.fr', '5610A', 'Restauration', '5610', NULL, 10, '1-10', 'Petite', '2018-03-15', NULL, NULL, 'HCR', 'RCS-69000-2018', '2018-04-01', NULL, 50000, FALSE, '30/06', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);

-- Insertion des établissements
INSERT INTO etablissement (type_etablissement, situation, ridet, designation, enseigne, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, date_creation, date_debut_activite, date_fin_activite, convention_collective, entreprise_id)
VALUES 
('Siège social', 'Actif', 'ETAB001', 'Siège de Tech Innovators', 'Tech Innov', '6201Z', 'Conseil en informatique', '6201', '6202', '10 Rue de la Technologie', '75001', 'Paris', '10 Rue de la Technologie', '75001', 'Paris', '2015-06-01', '2015-06-15', NULL, 'Syntec', 1);

INSERT INTO etablissement (type_etablissement, situation, ridet, designation, enseigne, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, date_creation, date_debut_activite, date_fin_activite, convention_collective, entreprise_id)
VALUES 
('Agence', 'Actif', 'ETAB002', 'Agence Cuisine Créative', 'Cuisine Créa', '5610A', 'Restauration rapide', '5610', NULL, '20 Avenue des Chefs', '69000', 'Lyon', '20 Avenue des Chefs', '69000', 'Lyon', '2018-03-15', '2018-04-01', NULL, 'HCR', 2);

-- Insertion des dirigeants
INSERT INTO dirigeant (role, nom, date_naissance, nationalite, adresse, code_postal, ville, titre_cma, date_de_fonction_rm, date_de_fonction_ra, situation_matrimoniale, maitre_apprentissage, qualifie_dans_son_metier, entreprise_id)
VALUES 
('Président', 'Dupont', '1980-05-12', 'Française', '10 Rue de la Technologie, Paris', '75001', 'Paris', 'N/A', '2015-06-01', NULL, 'Célibataire', 'Non', 'Oui', 5);

INSERT INTO dirigeant (role, nom, date_naissance, nationalite, adresse, code_postal, ville, titre_cma, date_de_fonction_rm, date_de_fonction_ra, situation_matrimoniale, maitre_apprentissage, qualifie_dans_son_metier, entreprise_id)
VALUES 
('Gérante', 'Martin', '1985-09-23', 'Française', '20 Avenue des Chefs, Lyon', '69000', 'Lyon', 'N/A', '2018-03-15', NULL, 'Marié', 'Oui', 'Oui', 6);

-- Insertion des indicateurs financiers
INSERT INTO indicateurs_financiers (date_cloture, chiffre_affaire, marge_brute, excedent_brut_exploitation, resultat_net, entreprise_id)
VALUES 
('2023-12-31', 2000000, 800000, 600000, 400000, 5);

INSERT INTO indicateurs_financiers (date_cloture, chiffre_affaire, marge_brute, excedent_brut_exploitation, resultat_net, entreprise_id)
VALUES 
('2023-06-30', 500000, 200000, 150000, 100000, 6);

-- Insertion des bilans
INSERT INTO bilan (comptes_annuels, actes, entreprise_id, etablissement_id)
VALUES 
('Année 2022', 'Comptes validés', 1, 1);

INSERT INTO bilan (comptes_annuels, actes, entreprise_id, etablissement_id)
VALUES 
('Année 2023', 'Comptes en cours', 2, 2);


-- Insertion de 20 entreprises
INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT003', 'Design Studio', 'DesignX', 'SAS', '15 Rue de la Créativité', '75002', 'Paris', '15 Rue de la Créativité', '75002', 'Paris', '0145234567', 'contact@designstudio.fr', '7410Z', 'Design graphique', '7410', NULL, 12, '11-50', 'Moyenne', '2016-01-10', NULL, NULL, 'Syntec', 'RCS-75002-2016', '2016-02-01', NULL, 75000, TRUE, '31/12', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);
  
INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT004', 'Green Solutions', 'EcoGreen', 'SARL', '30 Avenue des Écologistes', '69001', 'Lyon', '30 Avenue des Écologistes', '69001', 'Lyon', '0478123456', 'info@greensolutions.fr', '0220Z', 'Consulting environnemental', '0220', NULL, 20, '11-50', 'Moyenne', '2019-05-20', NULL, NULL, 'HCR', 'RCS-69001-2019', '2019-06-01', NULL, 200000, FALSE, '30/06', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT005', 'Health Innovations', 'HealthTech', 'SAS', '5 Boulevard de la Santé', '75003', 'Paris', '5 Boulevard de la Santé', '75003', 'Paris', '0145678901', 'contact@healthinnovations.fr', '8610Z', 'Technologie médicale', '8610', NULL, 30, '11-50', 'Moyenne', '2020-02-15', NULL, NULL, 'Syntec', 'RCS-75003-2020', '2020-03-01', NULL, 150000, TRUE, '31/12', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT006', 'FinTech Innovators', 'FinTechX', 'SARL', '8 Rue de l Investissement', '75004', 'Paris', '8 Rue de l Investissement', '75004', 'Paris', '0148901234', 'contact@fintechinnovators.fr', '6499Z', 'Services financiers', '6499', NULL, 15, '11-50', 'Moyenne', '2021-03-10', NULL, NULL, 'HCR', 'RCS-75004-2021', '2021-04-01', NULL, 300000, FALSE, '30/06', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT007', 'Creative Agency', 'Creatives', 'SAS', '25 Rue des Artistes', '75005', 'Paris', '25 Rue des Artistes', '75005', 'Paris', '0145678910', 'contact@creativeagency.fr', '7311Z', 'Publicité', '7311', NULL, 22, '11-50', 'Moyenne', '2018-07-12', NULL, NULL, 'Syntec', 'RCS-75005-2018', '2018-08-01', NULL, 100000, TRUE, '31/12', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT008', 'Digital Marketing', 'DigiMarket', 'SARL', '50 Boulevard du Numérique', '75006', 'Paris', '50 Boulevard du Numérique', '75006', 'Paris', '0145678920', 'contact@digimarket.fr', '7312Z', 'Marketing digital', '7312', NULL, 18, '11-50', 'Moyenne', '2017-04-20', NULL, NULL, 'HCR', 'RCS-75006-2017', '2017-05-01', NULL, 250000, TRUE, '30/06', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT009', 'E-Commerce Solutions', 'EcomSolutions', 'SAS', '33 Rue des Ventes', '75007', 'Paris', '33 Rue des Ventes', '75007', 'Paris', '0145678931', 'contact@ecomsolutions.fr', '4791A', 'Vente en ligne', '4791', NULL, 35, '11-50', 'Moyenne', '2019-08-15', NULL, NULL, 'Syntec', 'RCS-75007-2019', '2019-09-01', NULL, 500000, FALSE, '31/12', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT010', 'App Development', 'AppDev', 'SARL', '12 Rue des Applications', '75008', 'Paris', '12 Rue des Applications', '75008', 'Paris', '0145678942', 'contact@appdev.fr', '6202A', 'Développement d applications', '6202', NULL, 50, '51-100', 'Grande', '2020-09-10', NULL, NULL, 'HCR', 'RCS-75008-2020', '2020-10-01', NULL, 400000, TRUE, '30/06', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);


INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT011', 'Construction Group', 'BuildCo', 'SAS', '45 Rue des Bâtisseurs', '75009', 'Paris', '45 Rue des Bâtisseurs', '75009', 'Paris', '0145678953', 'contact@buildco.fr', '4120A', 'Construction', '4120', NULL, 60, '51-100', 'Grande', '2018-11-15', NULL, NULL, 'Syntec', 'RCS-75009-2018', '2018-12-01', NULL, 600000, TRUE, '31/12', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT012', 'Travel Agency', 'TravelMore', 'SARL', '19 Avenue des Voyages', '75010', 'Paris', '19 Avenue des Voyages', '75010', 'Paris', '0145678964', 'contact@travelmore.fr', '7911Z', 'Agences de voyages', '7911', NULL, 25, '11-50', 'Moyenne', '2015-01-20', NULL, NULL, 'HCR', 'RCS-75010-2015', '2015-02-01', NULL, 100000, FALSE, '30/06', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT013', 'Security Solutions', 'SecureCo', 'SAS', '28 Boulevard de la Sécurité', '75011', 'Paris', '28 Boulevard de la Sécurité', '75011', 'Paris', '0145678975', 'contact@secureco.fr', '8020Z', 'Services de sécurité', '8020', NULL, 15, '11-50', 'Moyenne', '2016-10-15', NULL, NULL, 'Syntec', 'RCS-75011-2016', '2016-11-01', NULL, 250000, TRUE, '31/12', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT014', 'Fashion Hub', 'FashionX', 'SARL', '60 Rue de la Mode', '75012', 'Paris', '60 Rue de la Mode', '75012', 'Paris', '0145678986', 'contact@fashionhub.fr', '4771Z', 'Commerce de détail', '4771', NULL, 20, '11-50', 'Moyenne', '2017-04-05', NULL, NULL, 'HCR', 'RCS-75012-2017', '2017-05-01', NULL, 150000, FALSE, '30/06', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT015', 'Real Estate Group', 'RealEstateCo', 'SAS', '77 Rue des Immeubles', '75013', 'Paris', '77 Rue des Immeubles', '75013', 'Paris', '0145678997', 'contact@realestateco.fr', '6810Z', 'Promotion immobilière', '6810', NULL, 50, '51-100', 'Grande', '2022-05-10', NULL, NULL, 'Syntec', 'RCS-75013-2022', '2022-06-01', NULL, 800000, TRUE, '31/12', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT016', 'Logistics Solutions', 'LogiCo', 'SARL', '99 Rue de la Logistique', '75014', 'Paris', '99 Rue de la Logistique', '75014', 'Paris', '0145678908', 'contact@logico.fr', '4941B', 'Transport et logistique', '4941', NULL, 40, '11-50', 'Moyenne', '2018-09-20', NULL, NULL, 'HCR', 'RCS-75014-2018', '2018-10-01', NULL, 500000, FALSE, '30/06', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT017', 'Consulting Group', 'ConsultX', 'SAS', '11 Avenue du Conseil', '75015', 'Paris', '11 Avenue du Conseil', '75015', 'Paris', '0145678919', 'contact@consultx.fr', '7022Z', 'Conseil en management', '7022', NULL, 23, '11-50', 'Moyenne', '2020-11-25', NULL, NULL, 'Syntec', 'RCS-75015-2020', '2020-12-01', NULL, 150000, TRUE, '31/12', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT018', 'Blockchain Solutions', 'BlockCo', 'SAS', '35 Rue des Technologies', '75016', 'Paris', '35 Rue des Technologies', '75016', 'Paris', '0145678923', 'contact@blockco.fr', '6201Z', 'Services informatiques', '6201', NULL, 12, '11-50', 'Moyenne', '2021-04-10', NULL, NULL, 'HCR', 'RCS-75016-2021', '2021-05-01', NULL, 250000, FALSE, '30/06', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT019', 'Gaming Solutions', 'GameX', 'SAS', '88 Rue du Jeu', '75017', 'Paris', '88 Rue du Jeu', '75017', 'Paris', '0145678924', 'contact@gamingx.fr', '5821Z', 'Développement de jeux', '5821', NULL, 30, '11-50', 'Moyenne', '2022-08-15', NULL, NULL, 'HCR', 'RCS-75017-2022', '2022-09-01', NULL, 500000, TRUE, '31/12', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO entreprise (rid, designation, enseigne, forme_juridique, adresse_physique, code_postal_physique, ville_physique, adresse_postale, code_postal_postale, ville_postale, telephone, email, code_ape, activites_secondaires, code_nafa, code_nafa_secondaires, nb_salaries, tranche_effectif_salaries, taille_structure, date_creation, date_radiation, motif_radiation, convention_collective, numero_rcs, date_immat_rcs, date_radiation_rsc, capital_social, capital_fixe, data_cloture_exercice_comptable, duree_personne_morale, numero_rm, date_immat_rm, date_radiation_rm, numero_rap, date_immat_rap, date_radiation_rap)
VALUES 
('ENT020', 'AI Innovations', 'AItech', 'SAS', '27 Rue de l Intelligence', '75018', 'Paris', '27 Rue de l Intelligence', '75018', 'Paris', '0145678925', 'contact@aitech.fr', '6202Z', 'Intelligence artificielle', '6202', NULL, 45, '11-50', 'Moyenne', '2021-05-20', NULL, NULL, 'Syntec', 'RCS-75018-2021', '2021-06-01', NULL, 600000, TRUE, '31/12', '99 ans', NULL, NULL, NULL, NULL, NULL, NULL;
