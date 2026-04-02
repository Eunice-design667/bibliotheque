<script setup lang="ts">
import {ref, onMounted } from 'vue'

interface Livre {
  id: number
  titre: string
  auteur: string
  disponible: boolean
}

const API_URL = 'http://127.0.0.1:8000/api/livres/'

const livres = ref<Livre[]>([])
const newLivre = ref<{ titre: string; auteur: string }>({ titre: '', auteur: '' })
const isEditing = ref(false)
const editingId = ref<number | null>(null)

// Pour recuperer les livres
const fetchLivres = async () => {
    try {
        const response = await fetch(API_URL)
        const result = await response.json()
        livres.value = result.data
    } catch (error) {
        console.error('Erreur fetch:', error)
    }
}

// Ajouter un livre
const createLivre = async () => {
    if (!newLivre.value.titre.trim() || !newLivre.value.auteur.trim()) return
    try {
        await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ titre: newLivre.value.titre, auteur: newLivre.value.auteur })
        })
        newLivre.value.titre = ''
        newLivre.value.auteur = ''
        await fetchLivres()
    } catch (error) {
        console.error('Erreur création:', error)
    }
}

// Preparer l'edition
const startEdit = (livre: Livre) => {
    isEditing.value = true
    editingId.value = livre.id
    newLivre.value.titre = livre.titre
    newLivre.value.auteur = livre.auteur
}

const updateUser = async () => {
    if (!editingId.value || !newLivre.value.titre.trim() || !newLivre.value.auteur.trim()) return
    try {
        await fetch(`${API_URL}${editingId.value}/`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ titre: newLivre.value.titre, auteur: newLivre.value.auteur })
        })
        cancelEdit()
        await fetchLivres()
    } catch (error) {
        console.error('Erreur mise à jour:', error)
    }
}

// Supprimer un livre
const deleteUser = async (id: number) => {
    if (!confirm('Supprimer ce livre ?')) return
    try {
        await fetch(`${API_URL}${id}/`, { method: 'DELETE' })
        await fetchLivres()
    } catch (error) {
        console.error('Erreur suppression:', error)
    }
}

// Annuler l'édition
const cancelEdit = () => {
    isEditing.value = false
    editingId.value = null
    newLivre.value.titre = ''
    newLivre.value.auteur = ''
}

const handleSubmit = () => {
    if (isEditing.value) {
        updateUser()
    } else {
        createLivre()
    }
}

onMounted(fetchLivres)
</script>

<template>
    <div class="page">
        <h1>Gestion des Livres</h1>
        <div class="card" style="padding: 20px; margin-bottom: 20px;">
            <h3>{{ isEditing ? 'Modifier le livre' : 'Ajouter un livre' }}</h3>
            <div class="form-grid" style="flex-direction: row; align-items: center; gap: 10px;">
                <input
                    v-model="newLivre.titre"
                    placeholder="Entrez le titre..."
                />
                <input
                    v-model="newLivre.auteur"
                    placeholder="Entrez l'auteur..."
                />
                <button @click="handleSubmit">{{ isEditing ? 'Mettre à jour' : 'Ajouter' }}</button>
                <button v-if="isEditing" @click="cancelEdit">Annuler</button>
            </div>
        </div>

        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr>
                    <th style="border-bottom: 1px solid #ccc; padding: 10px;">ID</th>
                    <th style="border-bottom: 1px solid #ccc; padding: 10px;">Titre</th>
                    <th style="border-bottom: 1px solid #ccc; padding: 10px;">Auteur</th>
                    <th style="border-bottom: 1px solid #ccc; padding: 10px; text-align: right;">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="livre in livres" :key="livre.id">
                    <td>{{ livre.id }}</td>
                    <td>{{ livre.titre }}</td>
                    <td>{{ livre.auteur }}</td>
                    <td style="text-align: right;">
                        <button @click="startEdit(livre)" style="margin-right: 10px; cursor: pointer;">✏️</button>
                        <button @click="deleteUser(livre.id)" style="cursor: pointer;">🗑️</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped>
/* .page {
  display: flex;
  font-family: 'Segoe UI', sans-serif;
  background: linear-gradient(135deg, #f0f4ff, #e8faff);
  min-height: 100vh;
} */

/* Sidebar colorée */
.sidebar {
  width: 220px;
  background: linear-gradient(180deg, #4f46e5, #9333ea);
  color: #fff;
  /* padding: 20px; */
  box-shadow: 2px 0 8px rgba(0,0,0,0.1);
}

.logo {
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 20px;
  text-align: center;
}

/* Boutons de navigation */
.sidebar button {
  display: block;
  width: 100%;
  padding: 12px;
  margin-bottom: 10px;
  text-align: left;
  border: none;
  background: rgba(255,255,255,0.1);
  color: #fff;
  cursor: pointer;
  border-radius: 6px;
  transition: background 0.3s;
}

.sidebar button:hover {
  background: rgba(255,255,255,0.25);
}

.sidebar button.active {
  background: #facc15;
  color: #1e293b;
  font-weight: bold;
}

/* Zone principale */
.main {
  flex: 1;
}

.content {
  padding: 30px;
}

/* Carte plus colorée */
.card {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  border-left: 6px solid #4f46e5;
  margin-bottom: 20px;
}

/* Table stylée */
table {
  width: 100%;
  border-collapse: collapse;
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
}

th {
  background: #4f46e5;
  color: #fff;
  padding: 12px;
  text-align: left;
}

td {
  padding: 12px;
  border-bottom: 1px solid #eee;
}

tr:hover {
  background: #f9fafb;
}

/* Inputs et boutons */
.form-grid {
  display: flex;
  flex-direction: row;
  gap: 10px;
  margin: 15px 0;
}

.form-grid input {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
  flex: 1;
}

button {
  background: #4f46e5;
  color: #fff;
  border: none;
  padding: 10px 15px;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.3s;
}

button:hover {
  background: #4338ca;
}

button.cancel {
  background: #ef4444;
}

button.cancel:hover {
  background: #dc2626;
}
</style>
