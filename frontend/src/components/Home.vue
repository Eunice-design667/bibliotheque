<script setup lang="ts">
// import LivreView from '@/views/LivreView.vue'
import { ref, onMounted } from 'vue'

interface User {
  id: number
  nom: string
}

const API_URL = 'http://127.0.0.1:8000/api/users/' 

const users = ref<User[]>([])
const newUser = ref<{ nom: string }>({ nom: '' })
const isEditing = ref(false)
const editingId = ref<number | null>(null)

// Récupérer les utilisateurs
const fetchUsers = async () => {
  try {
    const response = await fetch(API_URL)
    const result = await response.json()
    users.value = result.data
  } catch (error) {
    console.error('Erreur fetch:', error)
  }
}

// Ajouter un utilisateur
const createUser = async () => {
  if (!newUser.value.nom.trim()) return
  try {
    await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nom: newUser.value.nom })
    })
    newUser.value.nom = ''
    await fetchUsers()
  } catch (error) {
    console.error('Erreur création:', error)
  }
}

// Préparer l'édition
const startEdit = (user: User) => {
  isEditing.value = true
  editingId.value = user.id
  newUser.value.nom = user.nom
}

const updateUser = async () => {
  if (!editingId.value || !newUser.value.nom.trim()) return
  try {
    await fetch(`${API_URL}${editingId.value}/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nom: newUser.value.nom })
    })
    cancelEdit()
    await fetchUsers()
  } catch (error) {
    console.error('Erreur modification:', error)
  }
}

// Supprimer un utilisateur
const deleteUser = async (id: number) => {
  if (!confirm('Supprimer cet utilisateur ?')) return
  try {
    await fetch(`${API_URL}${id}/`, { method: 'DELETE' })
    await fetchUsers()
  } catch (error) {
    console.error('Erreur suppression:', error)
  }
}

// Annuler l'édition
const cancelEdit = () => {
  isEditing.value = false
  editingId.value = null
  newUser.value.nom = ''
}

const handleSubmit = () => {
  if (isEditing.value){
    updateUser()
  } else {
    createUser()
  }
}

onMounted(fetchUsers)
</script>

<template>
 
    <div class="main">
      <header class="topbar">
        <h1>Gestion des Utilisateurs</h1>
      </header>

      <main class="content">
        <div class="card" style="padding: 20px; margin-bottom: 20px;">
          <h3>{{ isEditing ? 'Modifier l\'utilisateur' : 'Ajouter un utilisateur' }}</h3>
          <div class="form-grid" style="flex-direction: row; align-items: center; gap: 10px;">
            <!--  v-model et @keyup.enter réactivés -->
            <input
              v-model="newUser.nom"
              placeholder="Entrez le nom..."
              @keyup.enter="handleSubmit"
            />
            <button class="btn-primary" @click="handleSubmit">
              {{ isEditing ? 'Mettre à jour' : 'Enregistrer' }}
            </button>
            <button v-if="isEditing" @click="cancelEdit" style="background: none; border: none; cursor: pointer;">
              Annuler
            </button>
          </div>
        </div>

        <div class="card">
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Nom</th>
                <th style="text-align: right;">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="user in users" :key="user.id">
                <td>{{ user.id }}</td>
                <td>{{ user.nom }}</td>
                <td style="text-align: right;">
                  <!--  Handlers ajoutés -->
                  <button @click="startEdit(user)" style="margin-right: 10px; cursor: pointer;">✏️</button>
                  <button @click="deleteUser(user.id)" style="cursor: pointer;">🗑️</button>
                </td>
              </tr>
              <tr v-if="users.length === 0">
                <td colspan="3" style="text-align: center; color: #999;">Aucun utilisateur trouvé.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </main>
    </div>
</template>

<style scoped>
.page { display: flex; font-family: sans-serif; background: #f4f7f6; min-height: 100vh; }
.sidebar { width: 200px; background: #fff; border-right: 1px solid #eee; padding: 20px; }
.sidebar button { display: block; width: 100%; padding: 10px; margin-bottom: 5px; text-align: left; border: none; background: none; cursor: pointer; border-radius: 5px; }
.sidebar button.active { background: #e0e7ff; color: #4f46e5; font-weight: bold; }
.main { flex: 1; }
.topbar { background: #fff; padding: 20px; display: flex; justify-content: space-between; border-bottom: 1px solid #eee; }
.content { padding: 20px; }
.card { background: #fff; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
table { width: 100%; border-collapse: collapse; }
th, td { padding: 12px; text-align: left; border-bottom: 1px solid #eee; }
.form-grid { display: flex; flex-direction: column; gap: 10px; margin: 15px 0; }
.form-grid input { padding: 8px; border: 1px solid #ddd; border-radius: 5px; }
.btn-primary { background: #4f46e5; color: #fff; border: none; padding: 10px 15px; border-radius: 5px; cursor: pointer; }
</style>