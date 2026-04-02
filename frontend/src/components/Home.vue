<script setup lang="ts">
import { ref, onMounted } from 'vue'


interface User {
    id: number
    nom: string
}

// 1. L'adresse de ton projet Django
const API_URL = 'http://127.0.0.1:5000/api/users/'

// Reactive variables
const users = ref<User[]>([])
const newUser = ref<User>({ id: 0, nom: '' })
const isEditing = ref(false)
// const editingId = ref<number | null>(null)
// const message = ref('')
// const showMessage = ref(false)
// Fetch users from the backend
const fetchUsers = async () => {    
    try {
        const response = await fetch(API_URL)
        users.value = await response.json()
    } catch (error) {
        console.error('Erreur lors de la récupération des utilisateurs:', error)
    }
}
onMounted(fetchUsers)

// Create a new user

</script>

<template>
  <div class="page">
    <aside class="sidebar">
      <div class="logo">📚 BiblioHub</div>
      <nav>
        <button class="active">👥 Utilisateurs</button>
      </nav>
    </aside>

    <div class="main">
      <header class="topbar">
        <h1>Gestion des Utilisateurs</h1>
      </header>

      <main class="content">
        <div class="card" style="padding: 20px; margin-bottom: 20px;">
          <h3>{{ isEditing ? 'Modifier l\'utilisateur' : 'Ajouter un utilisateur' }}</h3>
          <div class="form-grid" style="flex-direction: row; align-items: center; gap: 10px;">
            <input 
              v-model="newUser.nom" 
              placeholder="Entrez le nom..." 
              @keyup.enter=""
            />
            <button class="btn-primary" @click="">
              {{ isEditing ? 'Mettre à jour' : 'Enregistrer' }}
            </button>
            <button v-if="isEditing" @click="" style="background: none; border: none; cursor: pointer;">
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
                <td>#{{ user.id }}</td>
                <td>{{ user.nom }}</td>
                <td style="text-align: right;">
                  <button @click="" style="margin-right: 10px; cursor: pointer;">✏️</button>
                  <button @click="" style="cursor: pointer;">🗑️</button>
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
  </div>
</template>

<style scoped>
/* Styles de base pour la clarté */
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
.overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.5); display: flex; justify-content: center; align-items: center; }
.modal { background: #fff; padding: 25px; border-radius: 10px; width: 400px; }
.form-grid { display: flex; flex-direction: column; gap: 10px; margin: 15px 0; }
.form-grid input { padding: 8px; border: 1px solid #ddd; border-radius: 5px; }
.btn-primary { background: #4f46e5; color: #fff; border: none; padding: 10px 15px; border-radius: 5px; cursor: pointer; }
</style>