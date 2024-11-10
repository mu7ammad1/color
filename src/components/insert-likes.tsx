"use server";

import { sql } from "@vercel/postgres";

// دالة Server Action
export async function handleInsertLike(id: string) {
  try {
    // تنفيذ الاستعلام لإضافة أو تحديث سجل الإعجاب
    await sql`
      INSERT INTO likes (id, likes_count)
      VALUES (${id}, 1)
      ON CONFLICT (id)
      DO UPDATE 
      SET likes_count = likes.likes_count + 1
    `;
    console.log('Like added or updated successfully');
  } catch (error) {
    console.error("Error inserting like:", error);
  }
}
